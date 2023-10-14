import math
import matplotlib.pyplot as plt

while True:

    operation1 = {"add", "sub", "mul", "div"}
    operation2 = {"sqrt", "sqr", "cube", "log", "log base 10",
                  "log base 2", "log base e"}
    operation3 = {"line, scatter"}

    print(operation1)
    print(operation2)
    print(operation3)

    user_input = input("Choose an operation: ")

    if user_input in operation1:
        n1_str = (input("Enter the first number: "))
        n2_str = (input("Enter the second number: "))

        while not n1_str.isdigit():
            print("Invalid input, please enter a valid number for the first number.")
            n1_str = input("Enter the first number: ")

        while not n2_str.isdigit():
            print("Invalid input, please enter a valid number for the second number.")
            n2_str = input("Enter the second number: ")

        n1 = int(n1_str)
        n2 = int(n2_str)

        if user_input == "add":
            result = n1 + n2

        elif user_input == "sub":
            result = n1 - n2

        elif user_input == "mul":
            result = n1 * n2

        elif user_input == "div":
            result = n1 / n2

        if 'result' in locals() and result is not None:
            print("Result:", result)

    elif user_input in operation2:
        n1_str = (input("Enter the number: "))

        while not n1_str.isdigit():
            print("Invalid input, please enter a valid number.")
            n1_str = input("Enter the number: ")

        n1 = int(n1_str)

        if user_input == "sqrt":
            result = math.sqrt(n1)

        elif user_input == "sqr":
            result = n1 ** 2

        elif user_input == "cube":
            result = n1 ** 3

        elif user_input == "log":
            result = math.log(n1)

        elif user_input == "log base 10":
            result = math.log10(n1)

        elif user_input == "log base 2":
            result = math.log2(n1)

        elif user_input == "log base e":
            result = math.log(n1, math.e)

        if 'result' in locals() and result is not None:
            print("Result:", result)

    elif user_input == "line":
        x_str = input("Enter a list of x values separated by spaces: ")
        y_str = input("Enter a list of y values separated by spaces: ")
        x_values = [float(x) for x in x_str.split()]
        y_values = [float(y) for y in y_str.split()]
        plt.plot(x_values, y_values)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Line Graph")
        plt.show()

    elif user_input == "scatter":
        x_str = input("Enter a list of x values separated by spaces: ")
        y_str = input("Enter a list of y values separated by spaces: ")
        x_values = [float(x) for x in x_str.split()]
        y_values = [float(y) for y in y_str.split()]
        plt.scatter(x_values, y_values)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Scatter Plot")
        plt.show()


