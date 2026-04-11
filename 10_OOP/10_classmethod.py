class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )        
    
    @classmethod
    def from_string(cls, order_string):
        order_data = order_string.split(",")
        return cls(
            order_data[0],
            order_data[1],
            order_data[2]
        )
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large", "S", "M", "L", "s", "m", "l"]

order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": 10, "size": 200})
order2 = ChaiOrder.from_string("Masala,10,200")

order3 = ChaiOrder("Masala", 10, 200)

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

