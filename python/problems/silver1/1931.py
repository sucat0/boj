n = int(input())
timelist = []
for _ in range(n):
    starttime, endtime = map(int, input().split())
    timelist.append((starttime, endtime))

timelist.sort(key=lambda x: (x[1], -(x[1]-x[0])))

endtime_buff = 0
count = 0
for starttime, endtime in timelist:
    if starttime >= endtime_buff:
        endtime_buff = endtime
        count += 1
print(count)