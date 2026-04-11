#Attribute Shadowing
class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)
print(cutting.strength)

cutting.temperature = "mild"
cutting.cup = "small"
print("After changing:", cutting.temperature)
print("Cup size:", cutting.cup)
print("Direct look into the class:", Chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature) # falls back to the class attribute once we delete the instance attribute
print(cutting.cup)
