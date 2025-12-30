import random

try:
    difficulty = int(input("Welcome to the number guesser. Firstly, choose a difficulty:\n 1. (1 - 10)\n 2. (1 - 100)\n 3. (1 - 1000)\nYour choice: "))
except ValueError:
    print("You need to write the difficulty from 1 to 3.")
    exit()

if difficulty not in [1, 2, 3]:
    print("You need to write the difficulty from 1 to 3.")
    exit()

if difficulty == 1:
    number = random.randint(1, 10)
elif difficulty == 2:
    number = random.randint(1, 100)
else:
    number = random.randint(1, 1000)

tries = 0

while True:
    guess = int(input("Guess the number: "))
    tries += 1

    if guess < number:
        print("Your guess is smaller than the correct number!")
    elif guess > number:
        print("Your guess is bigger than the correct number")
    else:
        print(f"Yoohoo, you guessed it! It took you {tries} tries.")
        break
