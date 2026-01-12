def decorator(func):
    def wrapper(*args):
        print(f"before function")
        result = func(*args)
        print(f"after function")
        return result
    return wrapper
def add(a,b):
    return a+b
print(add(3,7))