def cache(func):
    dict = {}
    def wrapper(*args):
        