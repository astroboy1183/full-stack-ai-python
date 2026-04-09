'''A local cafe wants a program that suggests a snack.
If a customer asks for cookies or samosa, it confirms the order
Otherwise, it says it's not available.

Task:

Take snack input
If it's "cookies" or "samosa", confirm the order
Else, show unavailability'''

snack = input("Enter your preferred snack: ").lower()  # convert input to lowercase for case-insensitive comparison
print(f"User said: {snack}")

if snack == "cookies" or snack == "samosa":
    print(f"Order confirmed! We'll serve you {snack}.")
else:
    print("Sorry, that snack is not available.")