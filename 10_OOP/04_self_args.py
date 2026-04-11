class Chaicup:
    size = 150

    def describe(self):
        return f"A {self.size}ml chai cup."
    
cup = Chaicup()
print(cup.describe())# An object calls the method. 

print(Chaicup.describe(cup))# class calls the method, we need to pass the object.

cup_two = Chaicup()
cup_two.size = 200
print(cup_two.describe())
print(Chaicup.describe(cup_two))

    
