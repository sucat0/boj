from collections import deque


def find_route(a, b):
    queue = deque([b])
    count = 1

    while queue:
        num = queue.popleft()
        string_num = str(num)

        if num == a:
            return count

        if num < a:
            return -1

        if string_num[-1:] == '1' and len(string_num) > 1:
            queue.append(int(string_num[:-1]))
            count += 1

        if num % 2 == 0:
            queue.append(num // 2)
            count += 1

    return -1


a, b = map(int, input().split())
print(find_route(a, b))
