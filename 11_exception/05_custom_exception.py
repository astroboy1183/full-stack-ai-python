# use custom exception

def brew_chai(flavor):
    
    try:
        if flavor not in ["masala", "ginger", "lemon", "elaichi"]:
            raise ValueError(f"Unknown chai flavor: {flavor}")
    except ValueError as e:
        print("Error:",e)
    else:
        print(f"{flavor} chai is served.")
    finally:
        print("Next Customer Please.")

brew_chai("lemon")
brew_chai("unknown")
    