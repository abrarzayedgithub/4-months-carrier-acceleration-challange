dataset1 = [1,2,3,4,-1,-2]
dataset2 = [-3,4,5,6,7]
x = lambda x: x<0
y = lambda x: x>0
result1 = list(map(x,dataset1))
result2 = list(map(y,dataset2))
print(f"{any(result1)}")
print(f"{all(result2)}")