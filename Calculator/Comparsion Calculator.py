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