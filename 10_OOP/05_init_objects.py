class ChaiOrder:
    def __init__(self, type_, size, sugar):
        self.type = type_
        self.size = size
        self.sugar = sugar
    
    def summary(self):
        return f"{self.size}ml of {self.type} chai with {self.sugar} grams of sugar."

order = ChaiOrder("masala",200, 10)
print(order.summary())

order2 = ChaiOrder("ginger", 150, 5)
print(order2.summary())
    
