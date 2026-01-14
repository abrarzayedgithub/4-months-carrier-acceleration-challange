data = ["100x","20px","3px"]
print(f"{sorted(data,key=lambda x: int(x[:-2]))}")