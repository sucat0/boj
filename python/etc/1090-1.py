n = int(input())

win = 0

for _ in range(n):
    score = list(map(int, input().split()))
    run = score[:2]
    trick = score[2:]

    trick.sort(reverse=True)

    final = max(run) + trick[0] + trick[1]

    if final > win:
        win = final

print(win)
