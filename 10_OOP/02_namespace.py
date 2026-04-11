class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

#creating object
ginger_tea = Chai()
print(ginger_tea.origin)
print(ginger_tea.is_hot)
ginger_tea.is_hot = False
print(ginger_tea.is_hot)
ginger_tea.flavor = "ginger" #creating a new attribute just for ginger_tea.
print(ginger_tea.flavor)
# print(Chai.flavor)