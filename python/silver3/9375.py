from sys import stdin
read = stdin.readline

n = int(read().rstrip())

for _ in range(n):
    wears_num = int(read().rstrip())
    wears = {}
    wear_types = []

    if wears_num == 0:
        print('0')
        continue

    for _ in range(wears_num):
        wear, wear_type = read().split()

        if wear_type not in wears:
            wears[wear_type] = []
            wear_types.append(wear_type)
        
        wears[wear_type].append(wear)
    
    combination_count = 1
    for wear_type in wear_types:
        combination_count *= len(wears[wear_type]) + 1

    combination_count -= 1  # 알몸 제외
    print(combination_count)