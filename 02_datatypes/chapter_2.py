spicemix = set()
print(f"Initial Spice Mix: {id(spicemix)}")
print(f"Initial Spice Mix: {spicemix}")

spicemix.add("cumin")
spicemix.add("coriander")
print(f"Spice Mix Id after adding cumin and coriander: {id(spicemix)}")    
print(f"Spice Mix after adding cumin and coriander: {spicemix}")

#remove first element from the set
spicemix.pop()
print(f"Spice Mix Id after removing first element: {id(spicemix)}")
print(f"Spice Mix after removing first element: {spicemix}")

#add element in the beginning of the set
spicemix.add("turmeric")
print(f"Spice Mix Id after adding turmeric: {id(spicemix)}")
print(f"Spice Mix after adding turmeric: {spicemix}")