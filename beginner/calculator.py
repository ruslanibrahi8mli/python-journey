def calculator():
    while True:
        try:
            print("Welcome to Calculator!")
            num1 = int(input("First Number:  "))
            operation = input("Choose Your Operator (+, -, *, /, %, **): ")
            num2 = int(input("Second Number: "))

            if operation == "+":
                print(f"The Answer is: {num1 + num2}")
            elif operation == "-":
                print(f"The Answer is: {num1 - num2}")
            elif operation == "*":
                print(f"The Answer is: {num1 * num2}")
            elif operation == "/":
                print(f"The Answer is: {num1 / num2}")
            elif operation == "%":
                print(f"The Answer is: {num1 % num2}")
            elif operation == "**":
                print(f"The Answer is: {num1 ** num2}")
            else:
                print("Invalid operator!")

            exit_choice = input("Do You Wanna Exit? Y/N - ").upper()
            if exit_choice == "Y":
                break

        except ZeroDivisionError:
            print("Can't divide by zero!")

calculator()
