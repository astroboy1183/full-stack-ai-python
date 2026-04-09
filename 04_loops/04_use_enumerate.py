'''
You're creating a tea menu board.
Each item must be numbered.

Task:

Use enumerate() to print menu items with numbers.

'''
menu_items = ["Green Tea", "Black Tea", "White Tea", "Oolong Tea"]
for i, item in enumerate(menu_items, start=1):
    print(f"{i}. {item}")
