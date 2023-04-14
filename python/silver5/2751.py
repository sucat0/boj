from sys import stdin

n = int(stdin.readline())
num_list = [int(stdin.readline()) for _ in range(n)]

num_list.sort()

for num in num_list:
    print(num)