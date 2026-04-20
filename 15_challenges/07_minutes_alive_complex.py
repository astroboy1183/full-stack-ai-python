'''
Input:
Date of Birth
Time of birth

Output:
You are approximately:
- 9,131 days old
- 219,144 hours old
- 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
'''
# from ast import main
import datetime
import sys
import locale
locale.setlocale(locale.LC_ALL, '')

def minutes_alive(date_of_birth, time_of_birth):
    date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
    time_of_birth = datetime.datetime.strptime(time_of_birth, "%H:%M").time()

    print("*"*50)
    days = (datetime.datetime.now() - datetime.datetime.combine(date_of_birth, time_of_birth)).days
    hours = days * 24
    minutes = hours * 60
    print(f"You are approximately:\n- {days:,} days old\n- {hours:,} hours old\n- {minutes:,} minutes old")
    print("\nBonus:\n- Add comma formatting for large numbers\n- Let the user try again without restarting the program")
    print("*"*50)
    while True:
        choice = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if choice == "yes":
            date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
            time_of_birth = input("Enter your time of birth (HH:MM): ")
            minutes_alive(date_of_birth, time_of_birth)   
        else:    
            print("Goodbye!")
            sys.exit()


if __name__ == "__main__":
    date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
    time_of_birth = input("Enter your time of birth (HH:MM): ")
    minutes_alive(date_of_birth, time_of_birth)
    
    # print(date_of_birth)
    # print(time_of_birth)
    # print(datetime.datetime.combine(date_of_birth, time_of_birth))
    # print(datetime.datetime.now())
    # print(datetime.datetime.now() - datetime.datetime.combine(date_of_birth, time_of_birth))
    # print("*"*50)
    # print(type(date_of_birth))
    # print(type(time_of_birth))
    # print(type(datetime.datetime.combine(date_of_birth, time_of_birth)))
    # print(type(datetime.datetime.now()))
    # print(type(datetime.datetime.now() - datetime.datetime.combine(date_of_birth, time_of_birth)))