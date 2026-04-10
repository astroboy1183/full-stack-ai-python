def chai_customer():
    print("Customer: I would like to order a cup of chai.")
    order = yield "What flavor of chai would you like?"
    print(f"Customer: I would like {order} chai, please.")
    print(f"Preparing your {order} chai...")
    yield(f"Customer: Thank you for the {order} chai!")
customer = chai_customer()
print(next(customer)) # Start the generator and get the first prompt
print(customer.send("Masala")) # Send the flavor choice and get the preparation message

