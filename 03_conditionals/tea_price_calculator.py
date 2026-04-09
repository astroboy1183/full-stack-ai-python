'''A tea stall offers different prices for different cup sizes.
Write a program that calculates the price based on size.

Task:

Input: "small", "medium", "large"
Small → ₹10, Medium → ₹15, Large → ₹20
If invalid: show "Unknown cup size"'''
cup_size = input("Enter the cup size (small, medium, large): ").lower()  # convert input to lowercase for case-insensitive comparison
print(f"Cup size entered: {cup_size}")  
price = None  
if cup_size == "small" or cup_size == "s":
    price = 10
elif cup_size == "medium" or cup_size == "m":
    price = 15
elif cup_size == "large" or cup_size == "l":
    price = 20
else:    price = None

#print s as small, m as medium, l as large
if cup_size == "s":    
    cup_size = "small"
elif cup_size == "m":    
    cup_size = "medium"
elif cup_size == "l":    
    cup_size = "large"
else:
    cup_size = cup_size  # keep the original input for unknown sizes

if price is not None:
    print(f"The price for a {cup_size} cup of tea is: ₹{price}")
else:    print("Unknown cup size")


# #Get user input for number of cups of each size and calculate total price
# small_cups = int(input("Enter the number of small cups: "))
# medium_cups = int(input("Enter the number of medium cups: "))
# large_cups = int(input("Enter the number of large cups: "))
# small_price = 10
# medium_price = 15
# large_price = 20
# total_price = (small_cups * small_price) + (medium_cups * medium_price) + (large_cups * large_price)
# print(f"Total price for the order: ₹{total_price}")
