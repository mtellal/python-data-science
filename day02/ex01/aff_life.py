from load_csv import load
import matplotlib.pyplot as plt 







def main():
    file = load("life_expectancy_years.csv")
    
    dates = file[0, 1:]
    dates_x = [dates[x] for x in range(0, len(dates), 40)]
   
    ages = file[1, 1:]
    ages_y = [ages[x] for x in range(30, len(ages), 10)]

    print(ages_y)
    print(dates_x)

    plt.plot(dates_x, ages_y)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()

