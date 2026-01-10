def gen():
    yield 1
    yield 2

try:
    obj = gen()
    print(next(obj))
    print(next(obj))
    print(next(obj))
    print(next(obj))
except StopIteration:
    print("generator runs out of items")
    