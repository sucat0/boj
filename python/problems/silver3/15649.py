def permutation(n, r, current_index: int = 0, result_list: list = []):
    if current_index == r:
        yield ' '.join(map(str, result_list))

    else:
        for num in range(1, n+1):
            if num not in result_list:
                yield from permutation(n, r, current_index+1, result_list+[num])


def main():
    n, m = map(int, input().split())

    for nums in permutation(n, m):
        print(nums)


if __name__ == '__main__':
    main()