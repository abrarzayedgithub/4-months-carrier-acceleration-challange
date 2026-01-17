#fix a unicodedecodeError
try:
    with open ("file.txt",'r') as f:
        x = f.read()
        print(x)
except Unicodedecodeerror:
    print("always specifying utf-8 format")