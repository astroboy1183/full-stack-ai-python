value = 13
remainder = value % 5

if remainder:
    print(f"Not Divisible, remainder is {remainder}")


#using walrus operator
value=13
if remainder:=value%5:
    print(f"Not Divisible, remainder is {remainder}")

available_sizes = ["Small", "Medium", "Large"]

if (size := input("Enter the cup size (Small, Medium, Large): ")) in available_sizes:
    print(f"Great choice! A {size} cup of tea will be prepared for you.")
else:    print(f"Sorry, we don't have {size} size available. Please choose from Small, Medium, or Large.")

# ___________________________________________________________ 

flavors = ["Masala", "Ginger", "Cardamom", "Saffron"]
print("Available flavours:", flavors)

while (flavor:=input("Enter a flavour to add to the menu (or 'done' to finish): ")) not in flavors:
    print("Sorry, we don't have that flavour. Please choose from the available flavours.")

print(f"You chose {flavor} flavour.")



