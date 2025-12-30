def BMI_calculator():
    input("Hello! It's a BMI calculator. Press Enter to continue.\n")

    while True:
        try:
            height = float(input("Put your height (in cm) here: "))
            if height <= 0:
                print("Your height must be more than 0.")
                continue
            height /= 100 
            break
        except ValueError:
            print("Put a valid number.")

    while True:
        try:
            weight = float(input("Put your weight (in kg) here: "))
            if weight <= 0:
                print("Your weight must be more than 0.")
                continue
            break
        except ValueError:
            print("Put a valid number.")

    bmi = weight / (height ** 2)
    print(f'\nYour BMI is: {bmi:.2f}')

    if bmi < 18.5:
        print("You're underweight.")
    elif 18.5 <= bmi <= 24.9:
        print("You're normal weight.")
    elif 25 <= bmi <= 29.9:
        print("You're overweight.")
    elif 30 <= bmi <= 34.9:
        print("You're obese.")
    else:
        print("You're extremely obese.")

BMI_calculator()
