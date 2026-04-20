'''
Challenge: Friendship Compatibility Score
Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0–100).
3. Display the percentage with a themed message like:
     "You're like chai and samosa — made for each other!" or
     "Well... opposites attract, maybe?"

Bonus:
 Use emojis in the result.
 Give playful advice based on the score range.
 Capitalize and center the final output in a framed box.
'''
import string
import sys
import os
import random
from math import prod
import datetime
from itertools import product
import locale
locale.setlocale(locale.LC_ALL, '')

def calculate_compatibility_score(name1, name2):
    shared_letters = len(set(name1) & set(name2))
    shared_vowels = sum(1 for char in name1 if char in "aeiou") + sum(1 for char in name2 if char in "aeiou")
    shared_positions = sum(1 for i in range(min(len(name1), len(name2))) if name1[i] == name2[i])
    total_chars = len(name1) + len(name2)
    compatibility_score = (shared_letters + shared_vowels + shared_positions) / total_chars * 100
    return compatibility_score

if __name__ == "__main__":
    friend_a = input("Enter friend A's name: ").strip().lower()
    friend_b = input("Enter friend B's name: ").strip().lower()
    compatibility_score = calculate_compatibility_score(friend_a, friend_b)
    print("❤️ Friendship Calculator ❤️" )
    print(f"Your compatibility score is: {compatibility_score}%")
    if compatibility_score >= 50:
        print(f"You're like chai and samosa — made for each other! Your compatibility score is: {compatibility_score}%")
    else:
        print(f"Well... opposites attract, maybe? Your compatibility score is: {compatibility_score}%")
    print("*"*50)