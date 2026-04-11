#Project 1
print("MULTIPLICATION TABLE GENERATOR")
print("*" *30)

num  = int(input("Enter a number: "))
size = int(input("How many rows?: "))

print(f"\n{num} Times Tables:")
for i in range(1, size + 1):
    
    print(f"{num} X {i} = {num * i}")
