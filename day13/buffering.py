with open('file.txt','w') as f:
    for i in range(10000000):
        lines = f"line no {i+1}"
        f.write(lines)