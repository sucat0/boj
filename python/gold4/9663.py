from sys import stdin
from tabnanny import check


input = stdin.readline

n = int(input())
count = 0
queen_locations = [0] * n
check_col_queen = [False] * n

def check_ok(current_location):
    cx, cy = current_location

    for i in range(cy):
        qx = queen_locations[i]
        qy = i

        if qx == cx or abs(qx - cx) == abs(qy - cy): return False

    return True

def nqueen(row = 0):
    global count
    if row == n:
        count += 1
        return
    
    for i in range(n):
        if check_col_queen[i]:
            continue

        queen_locations[row] = i
        if check_ok((i, row)):
            check_col_queen[i] = True
            nqueen(row+1)
            check_col_queen[i] = False

nqueen()
print(count)