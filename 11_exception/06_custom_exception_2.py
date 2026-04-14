class OutOfIngredientsError(Exception): 
    pass

# def make_chai(milk, sugar):
#     try:
#         if milk == 0 or sugar == 0:
#             raise OutOfIngredientsError("Out of ingredients")
#     except OutOfIngredientsError as e:
#         print(e)
#     else:
#         print(f"Making chai with {milk} ml of milk and {sugar} grams of sugar.")

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Out of ingredients")
    print(f"Making chai with {milk} ml of milk and {sugar} grams of sugar.")

make_chai(milk=0, sugar=0)
make_chai(milk=100, sugar=50)        