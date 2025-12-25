numbers = list(range(10_000_000))
numbers_set = set(numbers)
if -5 in numbers_set:
    print("Found")
else:
    print("Not Found")
