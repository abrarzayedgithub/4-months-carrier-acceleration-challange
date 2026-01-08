from random import randint
list = [randint(1,20) for i in range(20)]
print(f"list{list}")
list.sort()
print(f"sorted list{list}")
