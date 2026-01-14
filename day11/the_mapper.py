square = lambda a: a**2
nums = [x for x in range(1,50)]
result = map(square,nums)
print(list(result))