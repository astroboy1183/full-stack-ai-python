class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala":20, "ginger":30, "cardamom":50}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Unknown chai flavor: {flavor}")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be an integer.")
        if cups <= 0:
            raise ValueError("Number of cups must be greater than 0.")
    except InvalidChaiError as e:
        print("Error:",e)
    except TypeError as e:
        print("Error:",e)
    except ValueError as e:
        print("Error:",e)
    else:
        print(f"{flavor} chai is served.")
        total = menu[flavor]*cups
        print(f"Total Bill for {cups} cups of {flavor} chai is rupees: {total}")
    finally:
        print("Next Customer Please.")


bill("ginger", 2)
bill("ginger", "2")
bill("ginger", 0)