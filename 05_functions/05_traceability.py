'''
Your shop adds a 10% VAT on every order.
You want this to be consistent and traceable.

Task:

Write add_vat(price, vat_rate)
Use it to compute final prices for 3 orders

'''

def add_vat(price, vat_rate):
    return price + (price * vat_rate / 100)

orders = [100, 200, 300]
vat_rate = 10 
for i, price in enumerate(orders, start=1):
    final_price = add_vat(price, vat_rate)
    print(f"Final price for order {i}: ₹{final_price}")