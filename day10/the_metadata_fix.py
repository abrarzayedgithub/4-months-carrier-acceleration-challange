def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper
@decorator
def greet():
    print("Hello, Data Science!")
greet()
print("Function name without wraps:", greet.__name__)
import functools
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper
def farewell():
    print("Goodbye, ML!")
farewell()
print("Function name with wraps:", farewell.__name__)

    
