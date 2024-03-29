import pandas as pd


"""
Return load function that load an csv file
"""


def load(path: str):
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it
    """
    try:
        assert type(path) is str, "invalid arg"
        file = pd.read_csv(path)
        np_array = file.to_numpy()
        print("Loading dataset of dimensions", np_array.shape)
        return file
    except Exception as msg:
        print("Error:", msg)
    return None


"""
print(load("life_expectancy_years.csv"), "\n")
print(load("population_total.csv"), "\n")
print(load("dfw"), "\n")
print(load([2, 3, 4]), "\n")
print(load(""), "\n")
print(load("life_expectancy_years_err.csv"), "\n")
print(load("e.csv"), "\n")
print(load(".csv"), "\n")
"""
