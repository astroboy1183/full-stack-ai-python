def update_order():
    chai_type = "Elaichi" # Local variable
    def kitchen():
        nonlocal chai_type # Refers to the nearest enclosing scope variable
        chai_type = "Masala" # Modifies the nonlocal variable
    kitchen()
    print(f"After kitchen: {chai_type}")
update_order()


