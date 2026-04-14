#raise multiple different exceptions

def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("a and b must be integers")
    else:
        print("Result is C:", c)
    finally:
        print("Thanks for using our calculator")

divide(2,3)
divide(2,0)
divide("2",3)
divide(2,"3")


print("***********************************************************************")
print("***********************************************************************")
print("***********************************************************************")
#raise multiple exceptions using raise
def divide(a, b):
    try:
        if b==0:
            raise ZeroDivisionError("Cannot divide by zero")
        if type(a) != int or type(b) != int:
            raise TypeError("a and b must be integers")
        c = a / b
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        print("Result is C:", c)
    finally:
        print("Thanks for using our calculator")

divide(2,3)
divide(2,0)
divide("2",3)
divide(2,"3")