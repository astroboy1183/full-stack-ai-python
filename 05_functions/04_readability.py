'''
You sell different chai sizes.
Instead of writing formulas everywhere, create a function.

Task:

Write calculate_bill(cups, price_per_cup)
Return total bill
Use this function for multiple orders

'''
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


order1 = calculate_bill(2, 10)
order2 = calculate_bill(1, 15)  
order3 = calculate_bill(3, 20)  
print(f"Total bill for order 1: ₹{order1}")
print(f"Total bill for order 2: ₹{order2}")
print(f"Total bill for order 3: ₹{order3}")