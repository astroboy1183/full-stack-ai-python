'''
💡 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200
People: Aman, Neha, Ravi

Final output:
Aman owes ₹400
Neha owes ₹400
Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
'''
names=[]
people = int(input("Enter Number of People: "))
for i in range(people):
    name = input("Enter Name: ")
    names.append(name)
bill = float(input("Total bill: ₹"))
print("People:", ", ".join(names))
share = bill / people
print(f"Each person owes: ₹{share}")

#check if numbers have more than 2 decimals
if share % 1 != 0:
    share = round(share, 2)
    print(f"Each person owes(rounding off to 2 decimal places): ₹{share}")

print("\nFinal Output:")
for name in names:
    print(f"{name} owes ₹{share}")

print("\nDecorative Summary Box:")
print("-" * 50)
for name in names:
    print(f"{name} owes ₹{share}")
print("-" * 50)