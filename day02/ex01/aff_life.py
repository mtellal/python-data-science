from load_csv import load
import matplotlib.pyplot as plt


"""
A program that calls the load function
from the previous exercise, loads the file
life_expectancy_years.csv, and displays
the country information of your campus. Your
graph must have a title and a legend for each axis.
"""


def main():
    try:
        file = load("life_expectancy_years.csv")
        if file is None:
            return
        dates = file[0, 1:]
        france_ages = []
        for row in file:
            if row[0] == "France":
                france_ages = row[1:].astype(float)
                break
        indexes = [i for i in range(0, len(france_ages), 40)]
        values = [dates[x] for x in indexes]
        plt.plot(dates, france_ages)
        plt.xticks(indexes, values)
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("France Life expectancy Projections")
        plt.show()
    except Exception as msg:
        print("Error:", msg)


if __name__ == "__main__":
    main()
