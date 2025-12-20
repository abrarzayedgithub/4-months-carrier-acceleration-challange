num = 123
temp = num 
rev = 0
while temp>0:
    rev = rev*10 + temp%10
    temp //= 10

if num == rev:
    print("palindrome")
else:
    print("not palidrome")