def combination(n: int, r: int, n_list: list, current_index: int = 0, result_list: list = []):
    if current_index == r:
        yield ' '.join(map(str, result_list))

    else:
        for num in n_list:
            if current_index == 0 or num > result_list[current_index-1]:
                yield from combination(n, r, n_list, current_index+1, result_list+[num])


def main():
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))


    for nums in combination(n, m, n_list):
        print(nums)


if __name__ == '__main__':
    main()