# from ctypes import Union
from os import POSIX_FADV_SEQUENTIAL
from pydoc import text
from unittest.mock import Base

from pydantic import BaseModel
from typing import List, Dict, Optional, Union

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address]=None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

class TextContent(BaseModel):
    type: str = "Text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    section: List[Union [TextContent, ImageContent]]

class Country(BaseModel):
    name: str
    code: str
class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class organization(BaseModel):
    name: str
    head_quarters: Address
    branches: List[Address] = []

# address = Address(street="123 Main St", city="Anytown", postal_code="12345")
# print(address)
# company = Company(name="Chaicode", address=address)
# print(company)
# employee = Employee(name="Jayanth Appalla", company=company)
# print(employee)



text_content = TextContent(content="This is a text content")
print(text_content)
image_content = ImageContent(url="https://example.com/image.jpg", alt_text="An image")
print(image_content)
article = Article(title="My Article", section=[text_content, image_content])
print(article)

country = Country(name="India", code="IN")
print(country)
state = State(name="Tamil Nadu", country=country)
print(state)
city = City(name="Chennai", state=state)
print(city)

address1 = Address(street="123 Main St", city=city, postal_code="12345")
print(address1)
organization = organization(name="Chaicode", head_quarters=address1, branches=[address1])
print(organization)


