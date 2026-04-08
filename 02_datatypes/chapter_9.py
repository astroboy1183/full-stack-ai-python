essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")
unique_essential_spices = essential_spices - optional_spices
print(f"Unique essential spices: {unique_essential_spices}")
unique_optional_spices = optional_spices - essential_spices
print(f"Unique optional spices: {unique_optional_spices}")

#membership test
print("Is cardamom an essential spice?", "cardamom" in essential_spices)
print("Is cardamom an optional spice?", "cardamom" in optional_spices)
print("Is black pepper an essential spice?", "black pepper" in essential_spices)
print("Is black pepper an optional spice?", "black pepper" in optional_spices)

# returns a new set with all unique elements from both sets
print(f"Union of spices: {essential_spices.union(optional_spices)}")  
print(f"Union of spices: {optional_spices.union(essential_spices)}")

#inplace set operations
essential_spices |= optional_spices   # union update
essential_spices &= optional_spices   # intersection update
essential_spices -= optional_spices   # difference update

# returns a new set with only the common elements from both sets
print(f"Intersection of spices: {essential_spices.intersection(optional_spices)}")
symmetric = essential_spices ^ optional_spices
print(f"Symmetric difference: {symmetric}")
unique_spices = essential_spices.symmetric_difference(optional_spices)
print(f"Unique spices in either set but not both: {unique_spices}")

#subset and superset tests
print(f"Is essential_spices a subset of optional_spices? {essential_spices.issubset(optional_spices)}")
print(f"Is essential_spices a superset of optional_spices? {essential_spices.issuperset(optional_spices)}")

essential_spices <= optional_spices   # subset
essential_spices >= optional_spices   # superset


#disjoint test
print(essential_spices.isdisjoint(optional_spices))

#modifying sets 
essential_spices.add("turmeric")
# essential_spices.remove("ginger")   # error if not present
essential_spices.discard("ginger")  # safe (no error)
print(f"Essential spices after modifications: {essential_spices}")

# pop and clear
spice = essential_spices.pop()  # removes random element
essential_spices.clear()        # removes all elements
print(f"Essential spices after popping and clearing: {essential_spices}")

essential_spices.add("cardamom")
essential_spices.add("cinnamon")
essential_spices.add("cloves")
essential_spices.add("ginger")
essential_spices.add("turmeric1")
print(f"Essential spices after adding cardamom and cinnamon: {essential_spices}")

#copying sets
new_set = essential_spices.copy()
print(f"New set copied from essential spices: {new_set}")

#frozenset - immutable set (Cannot modify , Can be used as dictionary keys, Hashable)
fs = frozenset(["cardamom", "ginger"])
print(f"Frozenset of spices: {fs}")

#set comprehension
lengths = {len(spice) for spice in essential_spices}
print(f"Lengths of essential spices: {lengths}")

#membership test for sets
if essential_spices & optional_spices:
    print("Some spices overlap")

print(f"Essential spices: {essential_spices}")
print(f"Optional spices: {optional_spices}")

essential_spices.update(optional_spices)  # union update
print(f"Essential spices after union update: {essential_spices}")