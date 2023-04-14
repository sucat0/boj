from itertools import product

def is_valid(i, num):
    c = 0
    for j in i:
        if int(num[c:c+j]) > 255:
            return False

        if (len(num[c:c+j]) != 1 and num[c:c+j][0] == '0'):
            return False

        c += j
    return True

num = input()
count = 0
for i in product(range(1, 4), repeat=4):
    if sum(i) == len(num):
        if is_valid(i, num):
            count += 1

print(count)