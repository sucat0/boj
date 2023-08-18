# Solved with pypy3
import sys

input = sys.stdin.readline
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
visited = [False for _ in range(26)]

board = [list(map(lambda x: ord(x) - ord('A'), list(input()))) for _ in range(R)]

def problem(r, c, count = 1):
    visited[board[r][c]] = True

    i = count
    for d in DIR:
        new_r, new_c = r+d[0], c+d[1]
        if 0 <= new_r < R and 0 <= new_c < C and visited[board[new_r][new_c]] == False:
            j = problem(new_r, new_c, count+1)
            if i < j: i = j

    visited[board[r][c]] = False

    return i

print(problem(0, 0))
