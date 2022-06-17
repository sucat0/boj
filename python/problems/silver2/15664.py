def combination(n, r, n_list, current_index=0, visited=None, *result):
    if visited is None:
        visited = [False] * n

    if current_index == r:
        yield ' '.join(map(str, result))

    else:
        prev_num = 0
        for num_index in range(n):
            num = n_list[num_index]

            if num != prev_num and (current_index == 0 or (not visited[num_index] and num >= result[current_index-1])):
                visited[num_index] = True
                prev_num = num

                yield from combination(n, r, n_list, current_index+1, visited, *result, num)

                visited[num_index] = False


def main():
    n, m = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))

    for nums in combination(n, m, n_list):
        print(nums)


if __name__ == '__main__':
    main()
