class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai)) # <class 'type'>, because Chai is a class, and all classes in Python are instances of the 'type' metaclass.

ginger_tea = Chai()
print(type(ginger_tea))  # <class '__main__.Chai'> 
print(type(ginger_tea) is Chai)  # True, because ginger_tea is an instance of the Chai class.
print(type(ginger_tea) is ChaiTime) 