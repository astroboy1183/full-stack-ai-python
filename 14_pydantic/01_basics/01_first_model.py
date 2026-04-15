from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':101, 'name':"chaicode", 'is_active':True}

# input_data1 = {'id':102, 'name':"chaicode", 'is_active':78}

input_data2 = {'id':"103", 'name':"chaicode", 'is_active':True} #converts id to int automatically

user = User(**input_data)
# user1 = User(**input_data1)
user2 = User(**input_data2)

print(user)
# print(user1)
print(user2)