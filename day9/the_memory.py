import sys

list_comprehension = [x for x in range(1000000)]
print(f"the list comprehension takes{sys.getsizeof(list_comprehension)}")

generator_expression = (x for x in range(1000000))
print(f"the generator takes{sys.getsizeof(generator_expression)}")