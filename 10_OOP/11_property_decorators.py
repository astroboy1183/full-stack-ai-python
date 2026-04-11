class TeaLeaf:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1<=age<=5:
            self._age = age
    
        else:
            raise ValueError("Age must be between 1 and 5.")

lead = TeaLeaf(2)
print(lead.age)

lead.age = 3
print(lead.age)   

lead.age = 4
print(lead.age)

lead.age = 6
print(lead.age)