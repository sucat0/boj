# 중복인 수 넣으면 다른 값 나옴 -> 틀렸습니다

from sys import stdin

class MinHeap:
    def __init__(self) -> None:
        self.heap = [0]

    def insert(self, num:int) -> None:
        self.heap.append(num)

        last_index = self.len()-1
        while last_index != 1 and num < self.heap[last_index//2]:
            self.heap[last_index], self.heap[last_index//2] = self.heap[last_index//2], self.heap[last_index]
            last_index //= 2

    def pop(self) -> int:
        if self.len()-1 == 0:
            return 0

        min = self.min()
        self._swap(1, -1)
        self.heap.pop()

        self._swap_all()
        
        return min

    def len(self) -> int:
        return len(self.heap)
    
    def min(self) -> None:
        return self.heap[1]

    def _swap_all(self) -> None:
        last_index = self.len()-1
        parent = 1
        while True:
            child = parent * 2
            if child < last_index and self.heap[child] > self.heap[child+1]:
                child += 1
            
            if child+1 >= last_index or self.heap[child] > self.heap[parent]:
                break
            
            self._swap(child, parent)
            parent = child

    def _swap(self, index_one, index_two) -> None:
        self.heap[index_one], self.heap[index_two] = self.heap[index_two], self.heap[index_one]

read = stdin.readline

n = int(read().rstrip())

min_heap = MinHeap()
for _ in range(n):
    x = int(read().rstrip())
    if x == 0:
        print(min_heap.pop())
    
    else:
        min_heap.insert(x)