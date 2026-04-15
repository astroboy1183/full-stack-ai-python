'''
Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
Name: Priya
Age: 22
City: Jaipur
Profession: Software Developer
Hobby: playing guitar

Your script might output:
"Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph (e.g., "Logged on: 2025-06-14")
- Wrap the printed message with a decorative border of stars (*)
'''
from datetime import date
import datetime
import sys


def get_string_input(prompt, max_invalid_attempts=13):
    attempts = 0
    while attempts < max_invalid_attempts:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
        elif not all(char.isalpha() or char.isspace() for char in user_input):
            print("Invalid input. Please enter text (letters and spaces only).")
        else:
            return user_input
        
        attempts += 1
        
        if attempts >= 10 and attempts < max_invalid_attempts: # Warn from 10th attempt up to the second-to-last attempt
            attempts_left = max_invalid_attempts - attempts
            print(f"You have entered an invalid format {attempts} times. You have {attempts_left} more attempts left.")
            
            # Ask to exit if attempts are 10, 11, or 12 (for max_invalid_attempts=13)
            if attempts >= (max_invalid_attempts - 3):
                exit_choice = input("You are about to reach the maximum number of invalid attempts. Do you want to exit? (yes/no): ").strip().lower()
                if exit_choice == 'yes':
                    sys.exit("Exiting program due to user input.")
        elif attempts == max_invalid_attempts:
            sys.exit(f"Exiting program due to persistent invalid inputs after {max_invalid_attempts} attempts.")
            
def get_int_input(prompt, max_invalid_attempts=13):
    attempts = 0
    while attempts < max_invalid_attempts:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
        else:
            try:
                int_value = int(user_input)
                return int_value
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        attempts += 1

        if attempts >= 10 and attempts < max_invalid_attempts: # Warn from 10th attempt up to the second-to-last attempt
            attempts_left = max_invalid_attempts - attempts
            print(f"You have entered an invalid format {attempts} times. You have {attempts_left} more attempts left.")
            
            # Ask to exit if attempts are 10, 11, or 12 (for max_invalid_attempts=13)
            if attempts >= (max_invalid_attempts - 3):
                exit_choice = input("You are about to reach the maximum number of invalid attempts. Do you want to exit? (yes/no): ").strip().lower()
                if exit_choice == 'yes':
                    sys.exit("Exiting program due to user input.")
        elif attempts == max_invalid_attempts:
            sys.exit(f"Exiting program due to persistent invalid inputs after {max_invalid_attempts} attempts.")

    sys.exit("Exiting program due to persistent invalid inputs.")


name = get_string_input("Enter your name: ")
name = " ".join(word.capitalize() for word in name.split()) #capitalize first letter of every word
age = get_int_input("Enter your age: ")
city = get_string_input("Enter your city: ")
city = " ".join(word.capitalize() for word in city.split())
profession = get_string_input("Enter your profession: ")
profession = " ".join(word.capitalize() for word in profession.split())
hobby = get_string_input("Enter your favorite hobby: ")
hobby = " ".join(word.capitalize() for word in hobby.split())

print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")

date = datetime.date.today().strftime("%Y-%m-%d")
print(f"Logged on: {date}")

print("*" * 50)
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print(f"Logged on: {date}")
print("*" * 50)
