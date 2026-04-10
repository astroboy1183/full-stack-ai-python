'''
Some chai flavors are out of stock.
You want to skip those and stop entirely if someone requests a restricted flavor.

Task:

Skip if flavor is "Out of Stock"
Break if flavor is "Discontinued"

'''
flavors = ["Masala Chai", "Ginger Chai", "Out of Stock", "Cardamom Chai", "Discontinued", "Saffron Chai"]
for flavor in flavors:
    if flavor == "Out of Stock":
        print(f"Sorry, flavor is currently out of stock. Going to the next flavor.")
        continue
    elif flavor == "Discontinued":
        print(f"Sorry, flavor has been discontinued. Stopping the menu.")
        break
    print(f"{flavor} is available.")

