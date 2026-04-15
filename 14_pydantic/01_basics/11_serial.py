from pydantic import BaseModel, ConfigDict, StrictStr
from typing import List, Dict, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    createdAt: datetime
    address: Optional[Address] = None
    tags: List[str] = []

    model_config = ConfigDict(json_encoders={
        datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
    })

# user = User(
#     id=1,
#     name="John Doe",
#     email="2kXx0@example.com",
#     is_active=True,
#     createdAt=datetime.now(),
#     address=Address(street="123 Main St", city="Anytown", postal_code="12345"),
#     tags=["tag1", "tag2"]
# )

# print(user.model_dump_json(indent=4))
# print(user)

user1 = User(
    id=2,
    name="Jane Doe",
    email="7K8r7@example.com",
    is_active=False,
    createdAt=datetime(2026, 4, 15, 17, 4, 0),
    address=Address(street="456 Elm St", city="Othertown", postal_code="54321"),
    tags=["tag3", "tag4"]
)

print(user1.model_dump())
print("*"*40)
print(user1.model_dump_json(indent=4))
print("*"*40)
print(user1)
