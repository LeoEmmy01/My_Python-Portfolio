# Age Calculator
print("\n" + "*"*40)
print("AGE CALCULATOR".center(40))
print("*"*40)

from datetime import date
birth_year = int(input("Enter Your Birth Year: "))
birth_month = int(input("Enter Your Month (1-12): "))
birth_day = int(input("Enter Your Birthday (1-31): "))

today = date.today()

birth_date = date(birth_year, birth_month, birth_day)

age_days = (today - birth_date).days

years = age_days // 365
month = (age_days % 365) // 30
days = (age_days % 365) % 30

print("\n" +"-"*40)
print("Your Age is:")
print("-"*40)

print(f"Year: {years}")
print(f"Months: {month}")
print(f"Days: {days}")
print(f"\n You are {years} years old, {month} months and {days} days old.")