# 11732번: 집합

# 그냥 일반적인 방법 사용하는게 나을듯......
from sys import stdin

m = int(stdin.readline())
s = set()

for _ in range(m):
    queue = stdin.readline().split()
    command = queue[0]
    if len(queue) == 1:
        if command == 'all':
            s = set(range(1, 21))

        elif command == 'empty':
            s = set()

    else:
        num = int(queue[1])
        if command == 'add':
            s.add(num)

        elif command == 'remove':
            s.discard(num)

        elif command == 'check':
            print(int(num in s))

        elif command == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)