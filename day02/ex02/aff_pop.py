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


def findRow(country: str, file: np.ndarray) -> np.ndarray:
    """
    From a file, iterate and file the country data
    Arguments:
        country (str): country str to match in rows[0]
        file (array): 2D array that corredonds to csv file
    Return:
        array: row data of float elements
    """
    for row in file:
        if row[0] == country:
            _row = []
            for e in row[1:]:
                if e[-1] == "M":
                    _row.append(int(float(e[:-1]) * 1000000))
                elif e[-1] == "k":
                    _row.append(int(float(e[:-1]) * 1000))
            _row = np.array(_row).astype(float)
            return _row
    return None


def formatLegend():
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [1, 0]
    handles_ordered = [handles[i] for i in order]
    labels_ordered = [labels[i] for i in order]
    plt.legend(handles_ordered, labels_ordered, loc="lower right")


def main():
    try:
        picked_country = "Belgium"
        if len(sys.argv) == 2:
            picked_country = sys.argv[1]
        file = load("population_total.csv")
        if file is None:
            return
        dates = file[0, 1:]
        dates = np.array([x for x in dates if int(x) <= 2050])

        france = findRow("France", file)
        france = france[:len(dates)]
        country = findRow(picked_country, file)
        if country is None:
            raise Exception("country '" + picked_country + "' not found")
        country = country[:len(dates)]
        country = np.resize(country, dates.shape) 
        plt.plot(dates, france, color="green", label="France")
        plt.plot(dates, country, color="blue", label=picked_country)

        xindexes = [i for i in range(0, len(france), 40)]
        xvalues = [dates[i] for i in xindexes]
        plt.xticks(xindexes, xvalues)
        
        max_value = 70 * 10**6
        max_value_country = np.amax(country)

        if max_value < max_value_country:
            max_value = max_value_country

        plt.ylim(0, max_value)
        yindexes = [i for i in range(0, int(max_value), int(max_value / 4))]
        yvalues = [str(int(i / 10**6)) + "M" for i in yindexes]
        plt.yticks(yindexes, yvalues)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        formatLegend()
        plt.show()
    except Exception as msg:
        print("Error:", msg)


if __name__ == "__main__":
    main()
