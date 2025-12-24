def read_thetas():
    try:
        file = open("thetas.txt", "r")
        content = file.read()
        thetas = content.split(sep="\n")
        return thetas
    except FileNotFoundError:
        return [0, 0]

def estimated_price(mileage, theta0, theta1):
    return float(theta0) + (float(theta1) * mileage)


def main():
    try:
        print("Provides mileage to estimate the price:")
        mileage = int(input())
        thetas = read_thetas()
        print(estimated_price(mileage, thetas[0], thetas[1]))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
