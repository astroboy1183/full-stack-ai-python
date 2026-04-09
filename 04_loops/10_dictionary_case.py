#Dictionary in place of match case

users = [{"id": 1, "total": 100, "coupon":"P20"}, {"id": 2, "total": 200, "coupon":"F10"},{"id": 3, "total": 150, "coupon":"P15"}]

discounts = {"P20": (0.2, 0), "F10": (0.5,0), "P15": (0,10)}#percentage discount, fixed discount

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