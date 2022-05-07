import heapq
from sys import stdin

read = stdin.readline

n = int(read().rstrip())

min_heap = []
for _ in range(n):
    x = int(read().rstrip())
    if x == 0:
        try:
            min_num = heapq.heappop(min_heap)
        except:
            min_num = 0
        
        print(min_num)
    
    else:
        heapq.heappush(min_heap, x)