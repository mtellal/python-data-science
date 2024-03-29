import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import sys


"""
A program that calls the load function from the first exercise,
loads the file population_total.csv, and displays the country
information of your campus versus other country of your choice.
Your graph must have a title, a legend for each axis and a
legend for each graph.
"""


def scale(value: str):
    """
    Transform a string to a float in the good scale
    (billion, millions, thousands ...)
    Arguments:
        value  (str): value to convert
    Return:
        float: the converted value
    """
    if value.endswith("B"):
        return float(value[:-1]) * 10**9
    elif value.endswith("M"):
        return float(value[:-1]) * 10**6
    elif value.endswith("k"):
        return float(value[:-1]) * 10**3
    else:
        return float(value)


def formatDatas(d: list, lim: int):
    """
    Convert each elements of a list and return it
    Arguments:
        d (list): list to convert
        lim (int): limit of the number of element in
        the list (used to normalise dates datas with rows)
    Return:
        List converted
    """
    return [scale(d.iloc[i]) for i in range(0, len(d)) if i < lim]


def main():
    try:
        p_country = "Belgium"
        if len(sys.argv) == 2:
            p_country = sys.argv[1]
        file = load("population_total.csv")
        if file is None:
            return
        dates = file.columns
        dates = [int(d) for d in dates if d != "country" and int(d) <= 2050]

        columns = ~file.columns.isin(["country"])
        france = file.loc[file.country == "France", columns].squeeze()
        france = formatDatas(france, len(dates))

        countries = file.loc[:, "country"]
        if p_country in countries.to_numpy():
            country = file.loc[file.country == p_country, columns].squeeze()
            country = formatDatas(country, len(dates))
        else:
            raise Exception("country '" + p_country + "' not found")

        plt.plot(dates, country, color="blue", label=p_country)
        plt.plot(dates, france, color="green", label="France")

        max_value = 70 * 10**6
        max_value_country = np.amax(country)

        if max_value < max_value_country:
            max_value = max_value_country

        plt.ylim(0, max_value)
        yindexes = [i for i in range(0, int(max_value), int(max_value / 4))]
        yvalues = [str(int(i / 10**6)) + "M" for i in yindexes]
        plt.yticks(yindexes, yvalues)

        plt.legend(loc="lower right")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()
    except Exception as msg:
        print("Error:", msg)


if __name__ == "__main__":
    main()
