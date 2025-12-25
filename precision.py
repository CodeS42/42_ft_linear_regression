import numpy as np


def estimated_prices(mileages, theta0, theta1):
    return [theta0 + (theta1 * m) for m in mileages]


def mean_absolute_error(est_prices, prices):
    return sum(abs(ep - p) for ep, p in zip(est_prices, prices)) / len(est_prices)


def calculate_average_prices(prices):
    return sum(prices) / len(prices)


def display_accuracy_percentage(mae, average_prices):
    percentage = 100 * (1 - mae / average_prices)
    print(f"The accuracy of the algorithm is {percentage:.2f}%.")


def main():
    try:
        with open("thetas.txt", "r") as file:
            thetas = file.read()
            thetas = [float(theta) for theta in thetas.split(sep="\n")]
        data = np.loadtxt("data.csv", delimiter=",", skiprows=1)
        mileages = data[:, 0]
        prices = data[:, 1]
        est_prices = estimated_prices(mileages, thetas[0], thetas[1])
        mae = mean_absolute_error(est_prices, prices)
        average_prices = calculate_average_prices(prices)
        display_accuracy_percentage(mae, average_prices)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
