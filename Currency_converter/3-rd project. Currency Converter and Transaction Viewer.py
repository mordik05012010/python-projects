import hashlib

# Dictionary to store users
users_db = {}
# Dictionary to store wallets
wallets = {}

# Custom exception for weak passwords
class WeakPasswordError(Exception):
    def __init__(self, message="Password does not meet security requirements"):
        super().__init__(message)

# Information about available currencies
currencies_info = {
    "UAH": {"description": "UAH (Ukrainian Hryvnia)", "rate": 1.0},
    "USD": {"description": "USD (US Dollar)", "rate": 0.02417},
    "EUR": {"description": "EUR (Euro)", "rate": 0.022},
    "GBP": {"description": "GBP (British Pound Sterling)", "rate": 0.019},
    "CNY": {"description": "CNY (Chinese Yuan)", "rate": 0.1762}
}

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a user
def register_user():
    username = input("Hello. Please enter your name: ").strip()
    if username in users_db:
        print("This username is already taken. Please choose another one.")
        return

    while True:
        password = input("Create a password: ")

        if len(password) < 10:
            print("The password must contain at least 10 characters.")
        elif not any(char.isupper() for char in password):
            print("The password must contain at least one uppercase letter.")
        elif not any(char.isdigit() for char in password):
            print("The password must contain at least one digit.")
        else:
            break

    users_db[username] = hash_password(password)
    wallets[username] = {code: 0.0 for code in currencies_info}  # Initialize an empty wallet
    print(f"Welcome, {username}!")

# Function to authenticate a user
def authenticate_user():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users_db and users_db[username] == hash_password(password):
        print(f"Welcome, {username}!")
        transactions(username, "User successfully logged in!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Function to show the wallet
def show_wallet(username):
    print(f"\nYour current wallet ({username}):")
    for code, balance in wallets[username].items():
        print(f"  {currencies_info[code]['description']}: {balance:.2f}")

# Function to convert currency
def convert_currency(username):
    show_wallet(username)
    
    from_curr = input("Enter the currency you want to convert from: ").strip().upper()
    to_curr = input("Enter the currency you want to convert to: ").strip().upper()

    if from_curr not in currencies_info or to_curr not in currencies_info:
        print("Error: Unknown currency entered!")
        return

    try:
        amount = float(input("Enter the amount to convert: "))
        if amount <= 0:
            print("The amount must be greater than zero!")
            return
        if wallets[username][from_curr] < amount:
            print("Insufficient funds!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return

    from_rate = currencies_info[from_curr]["rate"]
    to_rate = currencies_info[to_curr]["rate"]

    amount_in_uah = amount / from_rate
    converted_amount = amount_in_uah * to_rate

    wallets[username][from_curr] -= amount
    wallets[username][to_curr] += converted_amount
    print(f"Converted {amount:.2f} {from_curr} to {converted_amount:.2f} {to_curr} for {username}.")
    transactions(username, f"Converted {amount:.2f} {from_curr} to {converted_amount:.2f} {to_curr}.")

# Function to show available currencies
def show_curr_desc():
    print("\nAvailable currencies:")
    for code, data in currencies_info.items():
        print(f"  {code}: {data['description']}")

# Function to log transactions
def transactions(username, transaction):
    with open("transactions.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}: {transaction}\n")

# Function to add money to the wallet
def add_money(username):
    show_curr_desc()

    currency = input("Enter the currency to add: ").strip().upper()
    if currency not in currencies_info:
        print("Unknown currency!")
        return

    try:
        amount = float(input("Enter the amount to add: "))
        if amount <= 0:
            print("The amount must be greater than zero!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return

    wallets[username][currency] += amount
    print(f"Added {amount:.2f} {currency} to {username}'s wallet.")
    transactions(username, f"Added {amount:.2f} {currency}")

# Main loop
while True:
    action = input("\nChoose an action: 1. Register 2. Log in 3. Exit: ").strip()

    if action == "1":
        register_user()
    elif action == "2":
        username = authenticate_user()
        if username:
            while True:
                print("\nWhat would you like to do with your wallet?")
                print("1. Show current wallet")
                print("2. Add money to wallet")
                print("3. Convert money")
                print("4. Show available currencies")
                print("5. Log out of the wallet")

                choice = input("Choose an option: ").strip()

                if choice == "1":
                    show_wallet(username)
                elif choice == "2":
                    add_money(username)
                elif choice == "3":
                    convert_currency(username)
                elif choice == "4":
                    show_curr_desc()
                elif choice == "5":
                    print(f"Goodbye, {username}!")
                    transactions(username, "Logged out of the wallet")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif action == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
