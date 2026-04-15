from multiprocessing import Value

from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):

    username: str

    @field_validator("username")
    def validate_username(cls, value):
        if len(value) < 5:
            raise ValueError("Username must be at least 5 characters long")
        return value
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    # def check_passwords_match(cls, values):
    #     if values.password != values.confirm_password:
    #         raise ValueError("Passwords do not match")
    #     return values
    
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

signup = SignupData(password="secret123", confirm_password="secret123")
print(signup)

user = User(username="jayanth")
print(user)

# user1 = User(username="j")
# print(user1)

user2 = User(username="jayanthappalla")
print(user2)

user3 = User(username="jayanthappalla")
print(user3)
 
