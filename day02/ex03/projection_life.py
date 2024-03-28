import numpy as np
import matplotlib.pyplot as plt
from load_csv import load

def formatData(data: list[str]):
    final = []
    for e in data:
        if e[-1] == "M":
            final.append(int(float(e[:-1]) * 10**6))
        elif e[-1] == "k":
            final.append(int(float(e[:-1]) * 10**3))
    return final

def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    expectancy = load("life_expectancy_years.csv")
    
    if income is None or expectancy is None:
        return

    idx_1900 = np.where(income[0] == "1900")[0][0]
    income = [x[idx_1900] for x in income[1:]]
    income = np.array(income, int)

    idx_1900_2 = np.where(expectancy[0] == "1900")[0][0]
    expectancy = [x[idx_1900_2] for x in expectancy[1:]]

    final_expectancy = []
    final_income = []
    final_test = []
    lim = len(income)
    if len(expectancy) < lim:
        lim = len(expectancy)
    print(lim)
    for idx in range(0, lim):
        if expectancy[idx] != "" and income[idx] != "":
            final_income.append(income[idx])
            final_expectancy.append(expectancy[idx])
            final_test.append((income[idx], expectancy[idx]))
    final_expectancy = np.array(final_expectancy, float)

    zipped = list(zip(final_income, final_expectancy))

    zipped.sort(key=lambda x: x[0])
    final_income, final_expectancy = zip(*zipped)


    plt.plot(final_income, final_expectancy, 'bo')
    
    plt.xticks([300, 400, 500, 600, 700, 800, 900, 1000, 10000], ['300','400', '500', '600' , '700',  '800', '900', '1000', '10000'])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.show()
    

if __name__ == "__main__":
    main()
