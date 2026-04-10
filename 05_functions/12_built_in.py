def chai_flavor(flavor = "masala"):
    '''Returns a flavor of chai. Default is masala.'''
    return f"Here is your {flavor} chai."

print(chai_flavor())
print(chai_flavor.__doc__) #Accessing the docstring of the function
print(chai_flavor.__name__) #Accessing the name of the function. This is useful for debugging and logging purposes.
print(chai_flavor("ginger"))

def generate_bill(chai = 0, samosa = 0):
    '''Generates a bill for the given number of chai and samosa.
    param chai: number of chai ordered
    param samosa: number of samosa ordered
    return: total bill in rupees'''
    
    chai_price = 10
    samosa_price = 20
    total = (chai * chai_price) + (samosa * samosa_price)
    return f"Total bill: {total} rupees."
print(generate_bill(2, 3))
print(generate_bill.__doc__) 
print(generate_bill.__name__)


