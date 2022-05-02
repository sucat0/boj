dplist = {1:1, 2:2, 3:4, 4:7}

def splitdp(x):
    if x in dplist:
        return dplist[x]
    return splitdp(x-1) + splitdp(x-2) + splitdp(x-3)


t = int(input())
nlist = [int(input()) for _ in range(t)]

for n in nlist:
    print(splitdp(n))