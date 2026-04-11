# ATM Simulator
balance = 1000
correct_pin = "1234"
attempts = 0
max_attempts = 3

#Pin Validation
while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    
    if pin == correct_pin:
        print("Login sucessful ✅")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN ❌. Attempts left: {max_attempts - attempts}")
        
if attempts == max_attempts:
        print("Too many failed attempts. Account locked 🔒 ")
        exit()
else:
        #ATM Menu
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")
            
            choice = input("Choose an option (1-4): ")
            
            if choice == "1":
                print(f"Your balance is: ${balance}")
            
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                
                if amount <= 0:
                    print("Invalid amount❌ ")
                elif amount > balance:
                    print("Insufficient funds ❌ ")
                else:
                    balance -= amount
                    print(f"Withdrawal successful ✅")
            
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                
                if amount <= 0:
                    print("Cannot deposit negative or zero amount❌ ")
                else:
                    balance += amount
                    print(f"Deposit successful✅. New balance: ${balance}")
                    
            elif choice == "4":
                print("Thank you using the ATM👋 ")
                break
            
            else:
                print("Invalid option. please choose 1-4.")