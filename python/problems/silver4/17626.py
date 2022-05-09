num = int(input())

count = 0
while num > 0:
    sqrt_floor = int(num ** (1/2))
    print(sqrt_floor)
    num -= sqrt_floor ** 2
    count += 1

print(count)