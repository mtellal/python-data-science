import os
import csv
import numpy as np

"""
Return load function that load an csv file
"""


def load(path: str, display: bool = False) -> np.ndarray:
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it
    """
    try:
        assert type(path) is str, "invalid arg"
        split = os.path.splitext(path)
        if split[1] != ".csv":
            raise Exception("invalid extension" + split[1])
        with open(path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            final = []
            for row in csvreader:
                final.append(row)
                begin = row[0: 5]
                end = row[-5: len(row)]
                if display:
                    for x in begin:
                        print(str(x), end=' ')
                    print("...", end=' ')
                    for x in end:
                        print(str(x), end=' ')
                    print()
            return np.array(final)
    except Exception as msg:
        print("Error:", msg)


"""
print(load("life_expectancy_years.csv"), "\n")
print(load("dfw"), "\n")
print(load([2, 3, 4]), "\n")
print(load(""), "\n")
print(load("life_expectancy_years_err.csv"), "\n")
print(load("e.csv"), "\n")
print(load(".csv"), "\n")
"""
