numbers = [45,567,45,2,3,45,674,34,54]
max_val = numbers[0]
min_val = numbers[0]

for n in numbers:
    if n>max_val:
        max_val = n
    if n<min_val:
        min_val = n
print("max value:",max_val)
print("min value:",min_val)