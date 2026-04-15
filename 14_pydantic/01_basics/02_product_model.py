from math import prod

from pydantic  import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# Example usage:
product_data = {"id": 1, "name": "Chai Tea", "price": 15.50}
product_data1 = {"id": 2, "name": "Lemon Tea", "price": 18.50, "in_stock": False}
# product_data2 = {"name": "Ginger Tea"} # gives error

product = Product(**product_data)
product1 = Product(**product_data1)
# product2 = Product(**product_data2)

print(product)
print(product1)
# print(product2)

 


