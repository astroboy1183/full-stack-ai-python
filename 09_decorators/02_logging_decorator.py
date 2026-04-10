from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Logging activity: {func.__name__} was called with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log_activity
def brew_chai(chai_type):
    print(f"Brewing {chai_type} chai...")
brew_chai("Masala")
