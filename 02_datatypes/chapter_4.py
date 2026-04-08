is_boiling =   True
is_raining =   False
str_count = 5

total_actions = is_boiling + is_raining + str_count
print(f"Total actions: {total_actions}")

milk_present = 0 #{0,None is considered as False in boolean context}
print(f"Milk present: {bool(milk_present)}")

water_hot = True
tea_added = False
can_server = water_hot and tea_added
print(f"Can serve tea: {can_server}")