'''
Different Errors:

1. IndexError
2. ValueError
3. KeyError
4. TypeError
5. NameError
6. AttributeError
7. SyntaxError
8. IndentationError
9. RecursionError
10. ZeroDivisionError

'''

orders = ["masala","ginger"]

# print(orders[2])

#handle IndexError
try:
    print(orders[2])
except IndexError:
    print("Index out of range")