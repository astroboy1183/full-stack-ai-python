# from attr import field
from pydantic import BaseModel, field_validator, model_validator, ValidationError
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name","last_name")
    def names_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Names must be capitalized")
        return value
    
class User(BaseModel):
    email: str

    @field_validator("email")
    def normalize_email(cls, value):
        return value.lower().strip()
    
class Product(BaseModel):
    price: float

    @field_validator("price",mode="before")
    def convert_price_to_float(cls, value):
        if  not isinstance(value, float):
            return float(value.replace("$",""))
        return value

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode="after")
    def check_date_range(self):
        if self.start_date > self.end_date:
            raise ValueError("Start date must be before end date")
        return self


try:
    person = Person(first_name="jayanth", last_name="appalla")
    print(person)
except ValidationError as e:
    print("Person Validation Failed.")
    print(e.errors())


try:
    user = User(email="7K8r7@example.com")
    print(user)
except ValidationError as e:
    print("User Validation Failed.")
    print(e.errors())

try:
    product = Product(price="$99.99")
    print(product)
except ValidationError as e: 
    print("Product Validation Failed.")
    print(e.errors())

try:
    date_range = DateRange(start_date="2023-02-01", end_date="2023-01-01")
    print(date_range)
except ValidationError as e:
    print("Date Range Validation Failed.")
    print(e.errors())

# date_range = DateRange(start_date="2023-01-01", end_date="2023-02-01")
# print(date_range)



    