# 이중 우선순위 큐

from sys import stdin
import heapq

read = stdin.readline

t = int(read().rstrip())

for _ in range(t):
    k = int(read().rstrip())

    min_heap = []
    max_heap = []
    for _ in range(k):
        test_data = read().split()
        command, n = test_data[0], int(test_data[1])

        if command == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        
        if command == 'D':
            if len(max_heap) != 0:
                if n == 1:
                    max_num = -heapq.heappop(max_heap)
                    min_heap.remove(max_num)
                
                if n == -1:
                    min_num = heapq.heappop(min_heap)
                    max_heap.remove(-min_num)

    if len(max_heap) != 0:
        max_num = -max_heap[0]
        min_num = min_heap[0]
        print(max_num, min_num)
    else:
        print('EMPTY')