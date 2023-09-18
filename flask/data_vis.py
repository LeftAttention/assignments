from matplotlib import pyplot as plt

def main():

    y_values = [1, 3, 2, 4, 3, 5]
    x_values = list(range(1, len(y_values) + 1))

    plt.plot(x_values, y_values)

    plt.xlabel("X Values")
    plt.ylabel("Y Values")

    plt.show()

if __name__ == "__main__":
    main()