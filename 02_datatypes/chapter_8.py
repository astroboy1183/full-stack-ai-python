ingredients = ["water", "milk", "black tea"]

#append an element to the list
ingredients.append("sugar")

print(f"ingredients: {ingredients}")

#remove an element from the list
ingredients.remove("water")
print(f"ingredients after removing water: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

#extend the chai ingredients list with the spice options
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

#concatenate two lists
ch = spice_options + chai_ingredients
ch2 = chai_ingredients + spice_options
print(f"chai with spices: {ch}")
print(f"chai with spices (alternative): {ch2}")
print(f"chai ingredients: {chai_ingredients}")
print(f"spice options: {spice_options}")

#insert element at index 2
chai_ingredients.insert(2, "black tea")
print(f"chai ingredients after inserting black tea: {chai_ingredients}")

#remove element by index
del chai_ingredients[1]
print(f"chai ingredients after deleting element at index 1: {chai_ingredients}")

#remove last element
chai_ingredients.pop()
print(f"chai ingredients after popping last element: {chai_ingredients}")

#inplace reversal of the list
chai_ingredients.reverse() 
print(f"chai ingredients after reversing: {chai_ingredients}")

#reverse the list without modifying the original list
reversed_chai_ingredients = chai_ingredients[::-1]
print(f"reversed chai ingredients: {reversed_chai_ingredients}")
print(f"original chai ingredients: {chai_ingredients}")

#use sorted() to get a sorted version of the list without modifying the original list
sorted_chai_ingredients = sorted(chai_ingredients)
print(f"sorted chai ingredients: {sorted_chai_ingredients}")

#inplace sorting of the list
chai_ingredients.sort()
print(f"chai ingredients after sorting: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"sugar levels: {sugar_levels}")
print(f"max sugar level: {max(sugar_levels)}")
print(f"min sugar level: {min(sugar_levels)}")
print(f"sum of sugar levels: {sum(sugar_levels)}")
print(f"average sugar level: {sum(sugar_levels)/len(sugar_levels)}")
print(f"number of sugar levels: {len(sugar_levels)}")

sugar_levels.sort(reverse=True)
print(f"sugar levels sorted in descending order: {sugar_levels}")

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3 
print(f"strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARDA")
print(f"Modified Bytes: {raw_spice_data}")