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


name = input("Enter your name: ").strip()
name = " ".join(word.capitalize() for word in name.split()) #capitalize first letter of every word
age = int(input("Enter your age: ").strip())
city = input("Enter your city: ").strip()
city = " ".join(word.capitalize() for word in city.split())
profession = input("Enter your profession: ").strip()
profession = " ".join(word.capitalize() for word in profession.split())
hobby = input("Enter your favorite hobby: ").strip()
hobby = " ".join(word.capitalize() for word in hobby.split())

print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")

date = datetime.date.today().strftime("%Y-%m-%d")
print(f"Logged on: {date}")
print("*" * 50)
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print(f"Logged on: {date}")
print("*" * 50)
