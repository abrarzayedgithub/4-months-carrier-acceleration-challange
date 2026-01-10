def square(nums):
    for i in nums:
        yield i**2

def filter(nums):
    for i in nums:
        if i%2 == 0:
            yield i

nums = [1,2,3,4,5]
for i in filter(square(nums)):
    print(i)