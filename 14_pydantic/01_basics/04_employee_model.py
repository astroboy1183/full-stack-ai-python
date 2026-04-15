from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Jayanth Appalla"]        
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        gt = 10000,
        le = 100000,
        description="Employee Salary"
    )    

class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        description="User Email"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=20,
        description="User Password"
    )
    phone: str = Field(
        ...,
        pattern=r'^\d{10}$',
        description="User Phone Number"
    )
    age:int = Field(
        ...,
        gt = 18,
        le = 100,
        description="User Age"
    )
    discount: float = Field(
        ...,
        gt = 0,
        le = 100,
        description="User Discount"
    )

employee = Employee(id=1, name="Jayanth Appalla", department="IT", salary=50000)
user = User(email="7K8r7@example.com", password="password123", phone="1234567890", age=25, discount=10)

print(employee)
print(user)

