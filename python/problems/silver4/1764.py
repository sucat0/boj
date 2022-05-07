from sys import stdin

n, m = map(int, stdin.readline().split())

dutdo = set()
for _ in range(n):
    dutdo.add(stdin.readline().strip())

dutdo_bodo = []
count = 0
for _ in range(m):
    name = stdin.readline().strip()
    if name in dutdo:
        dutdo_bodo.append(name)
        count += 1

dutdo_bodo.sort()

print(count)
for index in range(count):
    print(dutdo_bodo[index])