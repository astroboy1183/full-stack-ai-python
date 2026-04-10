menu = [
    "Masala Chai",
    "Ginger Chai",  
    "Green Tea",    
    "Cardamom Chai",
    "Iced Lemon Tea",
    "Iced Peach Tea"
]

iced_teas = [flavor for flavor in menu if "Iced" in flavor]
print(f"Iced teas available: {iced_teas}")