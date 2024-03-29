import matplotlib.pyplot as plt
from load_csv import load


"""
A program that calls the load function from the first exercise,
loads the files
"income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
and "life_expectancy_years.csv",
and displays the projection of life expectancy in relation
to the gross national product of
the year 1900 for each country
"""


def main():
    file1 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income = load(file1)
    expectancy = load("life_expectancy_years.csv")

    income = income['1900']
    expectancy = expectancy['1900']

    plt.scatter(income, expectancy)
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1000", "10000"])
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == "__main__":
    main()
