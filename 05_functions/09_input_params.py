# chai = "Ginger Chai"

# def prepare_chai(order):
#     print(f"Preparing {order}.")
#     print(f"Finished preparing {order}.")

# prepare_chai(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup.append(4)
    cup[1]=54

edit_chai(chai)
print(f"Modified chai: {chai}")

def make_chai(tea, milk, sugar):
    print(f"Making chai : {tea}, {milk}, and {sugar}.")

make_chai("Darjeeling", "Yes", "Low")
make_chai(tea="Assam", sugar="High", milk="No") #keywords


def special_chai(*ingredients, **extras):
    print(f"Ingredients: {ingredients}")
    print(f"Type of ingredients: {type(ingredients)}")    
    print(f"Extras: {extras}")
    print(f"Type of extras: {type(extras)}")

special_chai("Cinnamon","Cardamom", sweetner = "Honey", foam = "Yes")


def chai_order(order=[]):
    order.append("Masala")
    print(f"Current order: {order}")
chai_order()
chai_order()

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Masala")
    print(f"Current order: {order}")

chai_order()
chai_order()