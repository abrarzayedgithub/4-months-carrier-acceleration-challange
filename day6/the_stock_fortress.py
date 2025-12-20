x = 20 
def change_x():
    global x
    x = 5
change_x()
print(f"x outside the function:",x)
  