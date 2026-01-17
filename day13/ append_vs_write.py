with open ('file.txt','w') as f:
    f.write('hellooo')

with open('file.txt','a') as f:
    f.write('abrar')
#with open('file.txt','r') as f:
    #x = f.read()
#print(x)
with open ('file.txt','x') as f:
    x = f.read()
print(x)
    
