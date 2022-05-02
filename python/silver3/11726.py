dpdict = {1:1, 2:2}

def tile(x):
    if x in dpdict:
        return dpdict[x]
    return tile(x-1) + tile(x-2)

i = int(input())
print(tile(i))