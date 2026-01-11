def decorator(func):
    def wrapper():
        print(f"tgis is a wrapper function")
        func()
        print(f"end of the wrapper function")
    return wrapper
@decorator
def hello():
    print("data science")