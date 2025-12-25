def read_thetas():
    try:
        with open("thetas.txt", "r") as file:
            content = file.read()
            thetas = [float(theta) for theta in content.split(sep="\n")]
        return thetas
    except FileNotFoundError:
        return [0, 0]

def estimated_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def main():
    try:
        print("Provides mileage to estimate the price:")
        mileage = float(input())
        if mileage < 0:
            raise ValueError("The mileage must be at least equal to 0.")
        thetas = read_thetas()
        print(estimated_price(mileage, thetas[0], thetas[1]))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
