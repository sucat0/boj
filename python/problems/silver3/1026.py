n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

result = 0
for a, b in zip(a, b):
    result += a * b
print(result)