n, m = map(int, input().split())


def allow_same_combination(n, r, current_index: int = 0, result_list: list = []):
    if current_index == r:
        yield ' '.join(map(str, result_list))

    else:
        for num in range(1, n+1):
            if current_index == 0 or num > result_list[current_index-1]:
                yield from allow_same_combination(n, r, current_index+1, result_list+[num])


for nums in allow_same_combination(n, m):
    print(nums)
