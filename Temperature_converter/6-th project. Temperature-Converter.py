try:
    taskbar_1 = int(input("Hello! This is a temperature converter. Please choose the temperature scale "
    "from which you want to convert:\n1. Celsius\n2. Fahrenheit\n3. Kelvin\nYour choice: "))

except ValueError:
    print("You need to write the temperature scale from 1 to 3.")
    exit()

if taskbar_1 == 1:
    taskbar_2 = int(input("Choose to which temperature scale you want to convert:\n1. Fahrenheit\n2. Kelvin\nYour choice: "))
    if taskbar_2 == 1:
        amount = float(input("Write the amount of the temperature: "))
        answer = amount * 9/5 + 32
        print(f"The answer is: {round(answer, 2)} Fahrenheit")
    if taskbar_2 == 2:
        amount = float(input("Write the amount of the temperature: "))
        answer = amount + 273.15
        print(f"The answer is: {round(answer, 2)} kelvin")

if taskbar_1 == 2:
    taskbar_2 = int(input("Choose to which temperature scale you want to convert:\n1. Celsius\n2. Kelvin\nYour choice: "))
    if taskbar_2 == 1:
        amount = float(input("Write the amount of the temperature: "))
        answer = (amount-32) * 5/9
        print(f"The answer is: {round(answer, 2)} Celsius")
    if taskbar_2 == 2:
        amount = float(input("Write the amount of the temperature: "))
        answer = (amount-32) * 5/9 + 273.15
        print(f"The answer is: {round(answer, 2)} Kelvin")

if taskbar_1 == 3:
    taskbar_2 = int(input("Choose to which temperature scale you want to convert:\n1. Celsius\n2. Fahrenheit\nYour choice: "))
    if taskbar_2 == 1:
        amount = float(input("Write the amount of the temperature: "))
        answer = amount - 273.15
        print(f"The answer is: {round(answer, 2)} Celsius")
    if taskbar_2 == 2:
        amount = float(input("Write the amount of the temperature: "))
        answer = (amount - 273.15) * 9/5 + 32
        print(f"The answer is: {round(answer, 2)} Fahrenheit")
