from logging import exception
from math import e


chai_menu = {"masala":40, "ginger":30, "cardamom":50}

print(chai_menu["masala"])

# print(chai_menu["Elaichi"]) #KeyError

#handle KeyError
try:
    print(chai_menu["Elaichi"])
except KeyError:
    print("Chai not available")

