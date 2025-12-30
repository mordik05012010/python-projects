from datetime import datetime

today = datetime.today()

birthday_year = int(input("Enter the year you were born: "))
birthday_month = int(input("Enter the month (e.g. May = 5): "))
birthday_day = int(input("Enter the day: "))

birth_date = datetime(birthday_year, birthday_month, birthday_day)

age_years = today.year - birth_date.year
age_months = today.month - birth_date.month
age_days = today.day - birth_date.day

if age_days < 0:
    age_months -= 1
    previous_month = (today.month - 1) if today.month > 1 else 12
    previous_month_year = today.year if today.month > 1 else today.year - 1
    days_in_prev_month = (datetime(today.year, today.month, 1) - datetime(previous_month_year, previous_month, 1)).days
    age_days += days_in_prev_month

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days.")
