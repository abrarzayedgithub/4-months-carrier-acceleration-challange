import time
start = time.time()
list_comp = [x**3 for x in range(10000)]
print(f"list_comp{time.time() - start}")
data = [x for x in range(10000)]
start = time.time()
x = lambda x:x**3
map_lambda = list(map(x,data))


print(f"map+lambda takes {time.time() - start}")