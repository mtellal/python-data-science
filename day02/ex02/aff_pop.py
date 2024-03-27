import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def findRow(country: str, file: np.ndarray) -> np.ndarray:
    for row in file:
        if row[0] == country:
            _row = []
            for e in row[1:]:
                if e[-1] == "M" or e[-1] == "k":
                    _row.append(e[:-1])
            _row = np.array(_row).astype(float)
            return _row


def main():
    try:
        file = load("population_total.csv")
        if file is None:
            return
        dates = file[0, 1:]
        dates = [x for x in dates if int(x) <= 2050]

        france = findRow("France", file)
        france = france[:len(dates)]
        belgium = findRow("Belgium", file)
        belgium = belgium[:len(dates)]
        plt.plot(dates, france, color="green", label="France")
        plt.plot(dates, belgium, color="blue", label="Belgium")

        xindexes = [i for i in range(0, len(france), 40)]
        xvalues = [dates[i] for i in xindexes]
        plt.xticks(xindexes, xvalues)

        plt.ylim(0, 70)
        yindexes = [20, 40, 60]
        yvalues = ["20M", "40M", "60M"]
        plt.yticks(yindexes, yvalues)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        handles, labels = plt.gca().get_legend_handles_labels()
        print(handles, labels)
        order = [1, 0]  # Spécifiez l'ordre des handles (France puis Belgium)
        plt.legend([handles[i] for i in order], [labels[i] for i in order])
        plt.legend(["Belgium", "France"], loc="lower right")
        plt.show()
    except Exception as msg:
        print("Error:", msg)


if __name__ == "__main__":
    main()
