nestedlist = [1,[2,[3,4]]]

def flatten(nestedlist):
    for i in nestedlist:
        if isinstance(i,list):
            yield from flatten(i)
        else:
            yield i

print(list(flatten(nestedlist)))