with open ('file.txt','w') as f:   #'file.txt' → ফাইলের নাম
    f.write('data science')         #w' → write mode


with open ('file.txt',"r") as f:
    x = f.read(4)

    print(x)