text = "banana"
A = {}
for char in text:
    if char in A:
        A[char] += 1
    else:
        A[char] = 1
print(A)