'''
You're building a simple app that registers users.
You want to separate concerns: getting input, validating it, and saving it.

Task:

Write register_user() that calls:
get_input()
validate_input()
save_to_db()

'''
def get_input():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    return name, email

def validate_input(name, email):
    if not name:
        print("Name cannot be empty.")
        return False
    if "@" not in email or "." not in email:
        print("Invalid email format.")
        return False
    return True

def save_to_db(name, email):
    print(f"Saving user to database: {name}, {email}")

def register_user():
    name, email = get_input()
    if validate_input(name, email):
        save_to_db(name, email)

register_user()
