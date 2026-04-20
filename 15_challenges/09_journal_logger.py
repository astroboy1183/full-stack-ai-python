'''
Challenge: Daily Learning Journal Logger
Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a .txt file along with a timestamp.

Your program should:

Ask the user what they learned today.
Add the entry to a file called learning_journal.txt.
Each entry should include the date and time it was written.
The journal should append new entries rather than overwrite.

Bonus:

Add an optional rating (1–5) for how productive the day was.
Show a confirmation message after saving the entry.
Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
'''
import datetime
from itertools import product
from math import prod
import os
import sys

def write_to_journal(entry,productivity_rating):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d — %I:%M %p")
    with open("learning_journal.txt", "a") as file:
        file.write(f"📅 {current_time}\n\n")
        file.write(f"{entry}\n\n")
        file.write(f"Productivity Rating: {productivity_rating}/5")
        file.write("\n")
        file.write("*"*50)
        file.write("\n")
    print("Entry saved successfully!")

def clear_journal():
    if os.path.exists("learning_journal.txt"):
        os.remove("learning_journal.txt")
        print("Journal cleared successfully!")
    else:
        print("Journal does not exist.")


if __name__ == "__main__":
    initial_choice = input("Do you want to clear the existing journal before starting? (yes/no): ").strip().lower()
    if initial_choice == "yes":
        clear_journal()
        print("Starting with a fresh journal.")
    elif initial_choice != "no":
        print("Invalid choice. Proceeding without clearing the journal.")

    while True:
        entry = input("Today I learned: ").strip()
        productivity_rating = input("Productivity Rating (1-5): ").strip()

        write_to_journal(entry,productivity_rating)

        choice = input("Do you want to add another entry? (yes/no): ").strip().lower()
        if choice != "yes":
            break