import numpy as np


def estimated_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)


def calculate_error(est_price, price):
    return est_price - price


def calculate_correction_theta0(learning_rate, m, errors):
    return learning_rate * (1 / m) * sum(errors)


def calculate_correction_theta1(learning_rate, m, errors, mileage):
    return learning_rate * (1 / m) * sum(errors * mileage)


def learning_loop(mileage, price):
    mileage_normalized = mileage / 100000
    price_normalized = price / 1000
    learning_rate = 0.05
    len_data = len(mileage)
    theta0 = 0
    theta1 = 0

    while True:
        est_prices = []
        errors = []
        for m in mileage_normalized:
            est_prices.append(estimated_price(theta0, theta1, m))
        for ep, p in zip(est_prices, price_normalized):
            errors.append(calculate_error(ep, p))
        tmp_theta0 = calculate_correction_theta0(learning_rate, len_data, errors)
        tmp_theta1 = calculate_correction_theta1(learning_rate, len_data, errors, mileage_normalized)
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
        if abs(tmp_theta0) < 0.0001 and abs(tmp_theta1) < 0.005:
            break
    
    theta0_denormalized = theta0 * 1000
    theta1_denormalized = theta1 * 0.01
    return [theta0_denormalized, theta1_denormalized]


def save_thetas(theta0, theta1):
    file = open("thetas.txt", "w")
    file.write(f"{theta0}\n")
    file.write(f"{theta1}\n")


def main():
    try:
        data = np.loadtxt("data.csv", skiprows=1, delimiter=",")
        mileage = data[:, 0]
        price = data[:, 1]
        thetas = learning_loop(mileage, price)
        save_thetas(thetas[0], thetas[1])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
