'''
Input:
Age: 25

Output:
You are approximately:
- 9,131 days old
- 219,144 hours old
- 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
'''
from ast import main
import sys
import locale
locale.setlocale(locale.LC_ALL, '')

def minutes_alive(age):
    days = age * 365
    hours = days * 24
    minutes = hours * 60

    print(f"You are approximately:\n- {days:,} days old\n- {hours:,} hours old\n- {minutes:,} minutes old")
    print("\nBonus:\n- Add comma formatting for large numbers\n- Let the user try again without restarting the program")

    while True:
        choice = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if choice == "yes":
            age = int(input("Enter your age: "))
            days = age * 365
            hours = days * 24
            minutes = hours * 60
            print(f"You are approximately:\n- {days:,} days old\n- {hours:,} hours old\n- {minutes:,} minutes old")
        else:
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    age = int(input("Enter your age: "))
    minutes_alive(age)