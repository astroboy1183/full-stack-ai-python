'''
Here is the extracted text from the images for your third Python challenge:

Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
Ask the user to input a password.
Tell them what's missing if it's weak.
If the password is strong, confirm it.
Suggest a strong random password if the input is weak.

Bonus:
Hide password input using `getpass` (no echo on screen).
'''
import getpass
import random
import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    if not any(char in string.punctuation for char in password):
        return "Weak: Password should contain at least one special character."
    return "Strong: Password meets all requirements."

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Strength Checker")
    password = getpass.getpass("Enter your password: ")
    result = check_password_strength(password)
    print(result)
    if "Weak" in result:
        print("Suggestion: Use a strong password with at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")
        random_password = generate_random_password()
        print(f"Randomly generated password: {random_password}")