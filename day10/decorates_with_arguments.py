def repeat(times=3):
    def inner(func):
        def wrapper(*args):
            for _ in range(times):
                func(*args)
        return wrapper
    return inner

@repeat(3)
def Data_science():
    print('Data_science')
Data_science()