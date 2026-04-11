# Basic Calculator
print("="*40)
print("BASIC CALCULATOR".center(40))
print("="*40)

#Get Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Performing Calculation
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
divsion = num1 / num2 if num2 !=0 else "Error: Division by zero"
floor_div = num1 // num2 if num2 != 0 else "Error"
modulus = num1 % num2 if num2 != 0 else "Error"
power = num1 ** num2

#Display Result
print("\n" + "-" * 40)
print("RESULT".center(40))
print("-"*40)
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {multiplication}")
print(f"{num1} // {num2} = {floor_div}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {power}")

#Advanced Calculator
#Calculator with comparison feature
print("\n" + "=" *40)
print("COMPARISON CALCULATOR".center(40))
print("="*40)

#Getting input value
a = float(input("Enter number A: "))
b = float(input("Enter number B: "))

#comparisons
print(f"\nComparing {a} and {b}:")
print(f"A equals B: {a == b}")
print(f"A not equal  to B: {a != b}")
print(f"A greater than B: {a > b}")
print(f"A less than B: {a < b}")
print(f"A great or less than B: {a >= b}")
print(f"A less or equal to B: {a <= b}")

#Logical operations
print(f"\nLogical Operations:")
print(f"(A > 0) and (B > 0): {(a > 0) and (b > 0)}")
print(f"(A > 0) or (B > 0): {(a > 0 ) or (b > 0)}")

print(f"not (A > B): {not(a > b)}")