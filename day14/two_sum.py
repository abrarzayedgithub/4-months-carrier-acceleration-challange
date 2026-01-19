x = [1,5,3,5,6]
y = 8

def twoSum(x,y):
    z = set()
    for i in x:
        if i in z:
            print(f"targeted num is{i} and needed num is {y - i}")
            return i,y - i
        z.add(y - i)
    print(f"two sum not possible")
twoSum(x,y)