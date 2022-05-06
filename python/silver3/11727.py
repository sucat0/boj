num_list = [1, 1, 3]
i = int(input())

for index in range(3, i+1):
    num_list.append(num_list[index-1] + num_list[index-2] * 2)

print(num_list[i] % 10007)