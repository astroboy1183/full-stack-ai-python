#types of functions:
#1. pure functions
#2. impure functions
#3. recursive functions
#4. lambda functions

def pure_chai(cups):
    return cups*10

total_chai = 0

#not recommended to use impure functions as they can lead to side effects and make code harder to debug and maintain
def impure_chai(cups):
    global total_chai
    total_chai += cups*10

def pour_chai(cups):
    if cups == 0:
        return "All cups poured."
    print(f"Pouring chai for {cups} cups.")
    return pour_chai(cups-1)

print(pour_chai(5))

chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda x: x != "kadak", chai_types))
print(f"Strong chai types: {strong_chai}")