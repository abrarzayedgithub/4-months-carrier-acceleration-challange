from functools import reduce
x = lambda a,b:a*b
data = [1,2,3,4]
result = reduce(x,data)
print(result)