from sys import stdin

read = stdin.readline
dp_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

t = int(read().rstrip())
n_list = [int(read().rstrip()) for _ in range(t)]

for index in range(5, max(n_list)-4):
    dp_list.append(dp_list[index] + dp_list[index+4])

for n in n_list:
    print(dp_list[n-1])