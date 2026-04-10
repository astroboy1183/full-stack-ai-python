daily_sales = [5, 10, 15, 20, 25, 8, 12, 18, 22, 30]

#how is this different from a list comprehension?
# A generator comprehension is more memory-efficient as it generates values on-demand, while a list comprehension creates the entire list in memory at once.

total_cups = sum(sale for sale in daily_sales if sale > 10 )

total_cups_list = sum([(sale) for sale in daily_sales if sale > 10])


print("Total cups sold (generator):", (total_cups))
print("Total cups sold (list):", (total_cups_list))

