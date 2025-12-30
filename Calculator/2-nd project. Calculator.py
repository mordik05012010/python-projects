try:
    num = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    countOperator = input("Enter your operator (+, -, *, /, **) :")

    if countOperator == "+":
        print("The answer is:", num + num2)
    elif countOperator == "-":
        print("The answer is:", num - num2)
    elif countOperator == "*":
        print("The answer is:", num * num2)
    elif countOperator == "/":
        if num2 != 0:
            print("The answer is:", num / num2)
        else:
            print("Division by zero is not allowed!")
    elif countOperator == "**":
        print("The answer is:", num ** num2)
    else:
        print("Wrong operation!")
except ValueError:
    print("Invalid input! Please enter numbers only.")
