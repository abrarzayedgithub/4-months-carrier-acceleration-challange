from random import randint
list = [randint(1,20000) for i in range(20000)]
print(f"list{list}")
slice = list[0:5000]
print(f"The sliced list{slice}")