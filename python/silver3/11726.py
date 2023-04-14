num_list = [1, 2]

i = int(input())-1

for index in range(1, i+1):
    num_list.append(num_list[index-1] + num_list[index])

print(num_list[i] % 10007)