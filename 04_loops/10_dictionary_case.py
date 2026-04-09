#Dictionary in place of match case

users = [{"id": 1, "total": 100, "coupon":"P20"}, {"id": 2, "total": 200, "coupon":"F10"},{"id": 3, "total": 150, "coupon":"P15"}]

discounts = {"P20": (0.2, 0), "F10": (0.5,0), "P15": (0,10)}#percentage discount, fixed discount

#solving this problem using match case would require a case for each coupon type, which is not scalable. Using a dictionary allows us to easily manage and apply discounts based on the coupon code without needing to modify the control flow structure for each new coupon type.

match users:
    case [{"id": id, "total": total, "coupon": "P20"}]:
        discount_amount = total * 0.2
        final_amount = total - discount_amount
        print(f"User {id} has a total of ₹{total} with coupon P20. Final amount after discount: ₹{final_amount}")
    case [{"id": id, "total": total, "coupon": "F10"}]:
        discount_amount = total * 0.5
        final_amount = total - discount_amount
        print(f"User {id} has a total of ₹{total} with coupon F10. Final amount after discount: ₹{final_amount}")
    case [{"id": id, "total": total, "coupon": "P15"}]:
        discount_amount = 10
        final_amount = total - discount_amount
        print(f"User {id} has a total of ₹{total} with coupon P15. Final amount after discount: ₹{final_amount}")
    case _:
        print("No valid coupons found for users.")

# Using a dictionary to store the discount information allows us to easily look up the discount for each coupon code without needing to write separate cases for each coupon type. This makes the code more maintainable and scalable as we can simply add new coupon types and their corresponding discounts to the dictionary without modifying the control flow structure.
for user in users:
    coupon = user["coupon"]
    total = user["total"]
    if coupon in discounts:
        percentage_discount, fixed_discount = discounts[coupon]
        discount_amount = total * percentage_discount + fixed_discount
        final_amount = total - discount_amount
        print(f"User {user['id']} has a total of ₹{total} with coupon {coupon}. Final amount after discount: ₹{final_amount}")
    else:
        print(f"User {user['id']} has a total of ₹{total} with no valid coupon. Final amount: ₹{total}")
