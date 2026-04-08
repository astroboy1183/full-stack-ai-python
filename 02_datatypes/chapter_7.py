masala_spices = ("cardamom", "cinnamon", "clove", "coriander", "cumin", "nutmeg", "pepper", "saffron", "turmeric")

#unpacking a tuple
(spice1, spice2, spice3, spice4, spice5, spice6, spice7, spice8, spice9) = masala_spices

print(f"Main spices in masala: {spice1}, {spice2}, {spice3}, {spice4}, {spice5}, {spice6}, {spice7}, {spice8}, {spice9}")

ginger_ratio, cardamom_ratio = 2, 1

print(f"Ratio is G:{ginger_ratio} and C:{cardamom_ratio}")

#swap ratio values
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping, Ratio is G:{ginger_ratio} and C:{cardamom_ratio}")

#membership

print("Is cardamom in masala spices?", "cardamom" in masala_spices)
print("Is pepper in masala spices?", "pepper" in masala_spices)
print("Is vanilla in masala spices?", "vanilla" in masala_spices)

