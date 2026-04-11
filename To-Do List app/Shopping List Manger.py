#SHOPPING LIST MANAGER

shopping_list = []

while True:
    print("\nSHOPPING LIST MANAGER")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Clear list")
    print("5. Exit")
    
    choice = input("Choose (1-5): ")
    
    if choice == "1":
        item = input("Item to add: ")
        shopping_list.append(item)
        print(f"Added {item}")
        
    elif choice == "2":
        if shopping_list:
            print(f"Items: {shopping_list}")
            item = input("Item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed {item}")
            else:
                print("Item not found")
        else:
            print("List is empty")
    
    elif choice == "3":
        if shopping_list:
            print("\nYour Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("List is empty")
                
    elif choice == "4":
        shopping_list.clear()
        print("List cleared")
        
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Ivalid choice")