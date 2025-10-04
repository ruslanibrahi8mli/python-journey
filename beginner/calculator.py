# Project: Calculator
# Date: 04.10.2025
# Description: My first calculator app


def calculator():
    while True:
        try:
            num1 = int(input("First Number: "))
            operation = input("Choose Your Operator (+, -, *, /, %, **): ")
            num2 = int(input("Second Number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            elif operation == "%":
                result = num1 % num2
            elif operation == "**":
                result = num1 ** num2
            else:
                print("Invalid operator!")
                continue

            print(f"The Answer is: {result}")

            exit_choice = input("Do You Wanna Exit? Y/N - ").upper()
            if exit_choice == "Y":
                break

        except ZeroDivisionError:
            print("Can't divide by zero!")

calculator()

