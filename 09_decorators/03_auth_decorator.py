from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user==("admin"):
            return func(user, *args, **kwargs)
        else:
            print("Access denied: Admin privileges required.")
    return wrapper

@require_admin
def access_sensitive_data(user):
    print("Accessing sensitive data...") 

# admin_user = {"username": "admin", "is_admin": True}
# regular_user = {"username": "user", "is_admin": False}
access_sensitive_data("admin")  # This will work
access_sensitive_data("user")  # This will print an access denied message

