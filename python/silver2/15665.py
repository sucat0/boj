def combination(n, r, n_list, current_index=0, *result):
    if current_index == r:
        yield ' '.join(map(str, result))

    else:
        prev_num = 0
        for num_index in range(n):
            num = n_list[num_index]

            if num != prev_num:
                prev_num = num

                yield from combination(n, r, n_list, current_index+1, *result, num)


def main():
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))

    for nums in combination(n, m, n_list):
        print(nums)


if __name__ == '__main__':
    main()
