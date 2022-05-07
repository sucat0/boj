from sys import stdin

read = stdin.readline

n, m = map(int, read().split())
nums = list(map(int, read().split()))

sumed_num = [nums[0]]
for index in range(1, n):
    sumed_num.append(sumed_num[index-1] + nums[index])

for _ in range(m):
    i, j = map(int, read().split())
    sum_num = sumed_num[j-1] if i == 1 else sumed_num[j-1] - sumed_num[i-2]
    print(sum_num)