#Discount Calculator
print("\n" + ">"*40)
print("DISCOUNT CALCULATOR".center(40))
print("<"*40)

original_price = float(input("Eneter the original price: "))
discount_percent = float(input("Enter your discount percentage: "))

disount_amount = (discount_percent / 100) * original_price

#Calculating for final price
final_price = original_price - disount_amount
print("\n" + "-"*40)
print ("Your Reciept")
print("-"*40)
print("Original price:{:>20.2f}".format(original_price))
print("Discount: {:20}%".format(discount_percent))
print ("You saved: {:>20.2f}".format(disount_amount))
print("Final price: {:>20.2f}".format(final_price))