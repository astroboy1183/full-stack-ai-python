'''
Ways of Accessing Base Class:

1. Code Duplication
2. Explicit Call
3. super()

'''
from typing import type_check_only


class Chai:

    def __init__(self, type_, strength):
        self.type = type_   
        self.strength = strength
    

# class GingerChai(Chai): #code duplication
    
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = self.spice_level

# class GingerChai(Chai): #explicit call
    
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(type_, strength)
#         self.spice_level = spice_level

class GingerChai(Chai): #super method
    
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level