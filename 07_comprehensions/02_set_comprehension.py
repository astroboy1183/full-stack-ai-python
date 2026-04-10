favourite_chais = ["Elaichi", "Ginger", "Masala", 
                   "Tulsi", "Lemon", "Ginger", "Elaichi"
                   ]

print(set(favourite_chais))

#remove duplicates
unique_chais = {chai for chai in favourite_chais}
print(unique_chais)

long_chais = {chai for chai in favourite_chais if len(chai) > 6}
print(long_chais)

recipes = {
    "Masala chai":["ginger", "cardamom", "cloves", "cinnamon"],
    "Ginger chai":["ginger", "cardamom"],
    "Elaichi chai":["elaichi", "cloves"],
    "Tulsi chai":["tulsi", "cardamom", "cloves"],
}

chai_ingredients = {ingredient for recipe in recipes.values() for ingredient in recipe}
print(chai_ingredients)