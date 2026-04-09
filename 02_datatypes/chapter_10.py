chai_order = dict(type = "Masala chai", size = "Large", sugar = 3)

# #add elements to dictionary
# chai_order["milk"] = "whole"
# chai_order["cardamom"] = "crushed"

# #add elements to dictionary using update() method
# chai_order.update({"milk": "whole", "cardamom": "crushed"})

print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"chai recipe: {chai_recipe}")
print(f"base of chai: {chai_recipe['base']}")

del chai_recipe["liquid"]
print(f"chai recipe after deleting liquid: {chai_recipe}")

#membership test
print("Is 'base' in chai recipe?", "base" in chai_recipe)
print("Is 'liquid' in chai recipe?", "liquid" in chai_recipe)
print("Is sugar in chai order?", "sugar" in chai_order)
print("Is size in chai order?", "size" in chai_order)

chai_order = {"type": "Masala chai", "size": "Large", "sugar": 3}

print(f"order details: {chai_order.keys()}")
print(f"order values: {chai_order.values()}")
print(f"order items: {chai_order.items()}")

print(f"chai order before popping an item: {chai_order}")
popped_item = chai_order.popitem()  # removes and returns the last inserted key-value pair
print(f"chai order after popping an item: {chai_order}")
print(f"popped item: {popped_item}")

chai_order.clear()  # removes all items from the dictionary
print(f"chai order after clearing: {chai_order}")

chai_order["type"] = "Ginger chai"
chai_order["size"] = "Medium"
chai_order["sugar"] = 2
print(f"chai order after adding new items: {chai_order}")

copy = chai_order.copy()  # creates a shallow copy of the dictionary
print(f"copy of chai order: {copy}")

copy.popitem()  # modifies the copy, not the original
print(f"copy after popping an item: {copy}")
print(f"original chai order after popping an item from copy: {chai_order}")

print(f"chai order : {chai_order}")
chai_order.pop("size")  # removes the key "size" and its associated value
print(f"chai order after popping 'size': {chai_order}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_order.update(extra_spices)  # adds key-value pairs from extra_spices to chai
print(f"chai order after updating with extra spices: {chai_order}")

print(f"chai order : {chai_order}")
chai_size = chai_order.get("size", "Size not specified")  # returns the value for "size" or a default message if "size" is not present
chai_cardamom = chai_order.get("cardamom", "Cardamom not specified")  # returns the value for "cardamom" or a default message if "cardamom" is not present
print(f"chai size: {chai_size}")
print(f"chai cardamom: {chai_cardamom}")

chai_order_new = chai_order.fromkeys(["size", "sugar"], "unknown")  # creates a new dictionary with specified keys and a default value
print(f"new chai order with default values: {chai_order_new}")

profile = dict.fromkeys(["name", "age", "occupation"], "not specified")
print(f"profile: {profile}")