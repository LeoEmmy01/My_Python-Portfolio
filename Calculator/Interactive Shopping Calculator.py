#Interactive Shopping Calculator
print("\n" + "="*40)
print("SHOPPING CALCULATOR".center(40))
print("="*40)

#Initial Input
budget = float(input("Enter your budget: $"))
print (f"Initial budget: ${budget}")

#add money to budget (using +=)
extra_money = float(input("Enter additional money received: $"))
budget += extra_money
print(f"Budget after addition: ${budget}")

#spend moeny (using -=)
item_price = float(input("Enter price of item to buy: $"))
if item_price <= budget:
    budget -= item_price
    print(f"Purchase successful! Remaining budget: ${budget}")
else:
    print("Insufficient funds!")
    
#Double remianing budget (using *=)
double = input("Do you want to double your remaining budget? (yes/no): ")
if double.lower() == "yes":
    budget *= 2
    print(f"Budget double New: ${budget}")
