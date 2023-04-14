def hanoi(src, dst, remain):
    if (remain == 0):
        return
    hanoi(src, 6-src-dst, remain-1)
    print(src, dst)
    hanoi(6-src-dst, dst, remain-1)

n = int(input())
print(2**n - 1)
hanoi(1, 3, n)