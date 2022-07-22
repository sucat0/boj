from collections import deque


class Const:
    MAX = 100000


def seek(n, k):
    if n > k:
        return n-k
    
    min_time = [-1] * (Const.MAX+1) 
    min_time[n] = 0

    calc_queue = deque([n])

    while calc_queue:
        calc = calc_queue.popleft()

        if calc == k:
            return min_time[k]

        if 0 <= calc*2 <= Const.MAX and min_time[calc*2] == -1:
            min_time[calc*2] = min_time[calc]
            calc_queue.appendleft(calc*2)

        if 0 <= calc+1 <= Const.MAX and min_time[calc+1] == -1:
            min_time[calc+1] = min_time[calc] + 1
            calc_queue.append(calc+1)

        if 0 < calc-1 <= Const.MAX and min_time[calc-1] == -1:
            min_time[calc-1] = min_time[calc] + 1
            calc_queue.append(calc-1)


n, k = map(int, input().split())

print(seek(n, k))
