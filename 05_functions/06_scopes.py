def serve_chai():
    flavor = "Masala Chai" #local scope
    print(f"Serving {flavor}.")

flavor = "Ginger Chai" #global scope
serve_chai()
print(f"Outside function: {flavor}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope

    def print_order():
        chai_order = "Masala"
        print(f"Inner: {chai_order}")    
    print_order()
    print(f"Outer: {chai_order}")
chai_order = "Tulsi"
chai_counter()
print(f"Global: {chai_order}")

