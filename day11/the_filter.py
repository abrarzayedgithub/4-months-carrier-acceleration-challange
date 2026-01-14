import random 
remove = lambda a:a>= 0
data = [random.randint(-5,5) for i in range(5)]
result = filter(remove,data)

print(list(result))