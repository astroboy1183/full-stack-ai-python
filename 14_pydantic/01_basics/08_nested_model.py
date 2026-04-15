from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Optional[Address] = None

address = Address(street="123 Main St", city="Anytown", postal_code="12345")
print(address)

user = User(id = 1 , name = "Jayanth Appalla", address = address)
print(user.model_dump_json(indent=4))
print(user)

#another way of initializing a nested model. 
data = {
    "id": 2,
    "name": "John Doe",
    "address": {
        "street": "132 Main St",
        "city": "Townsville",
        "postal_code": "12645"
    }
}

user_data = User(**data)
print(user_data)
