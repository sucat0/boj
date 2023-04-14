from itertools import product
from copy import deepcopy


dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
office_checked = []
min_count = 64

def check_cctv(x, y, dir_selection):
    while(True):
        x += dir_x[dir_selection]
        y += dir_y[dir_selection]

        if (x > n-1 or y > m-1 or x < 0 or y < 0): return
        if (office_checked[x][y] == 6): return
        if (office_checked[x][y] != 0): continue

        office_checked[x][y] = 7

cctv = []
for x, office_row in enumerate(office):
    for y, num in enumerate(office_row):
        if (not (num == 0 or num == 6)):
            cctv.append([x, y])

for _select_num_list in product([0, 1, 2, 3], repeat=len(cctv)):
    office_checked = deepcopy(office)

    for cctv_num, select_num in enumerate(_select_num_list):
        x, y = cctv[cctv_num]
        cctv_model = office[x][y]

        match cctv_model:
            case 1:
                check_cctv(x, y, select_num)

            case 2:
                check_cctv(x, y, select_num)
                check_cctv(x, y, (select_num+2)%4)

            case 3:
                check_cctv(x, y, select_num)
                check_cctv(x, y, (select_num+1)%4)
            
            case 4:
                check_cctv(x, y, select_num)
                check_cctv(x, y, (select_num+1)%4)
                check_cctv(x, y, (select_num+2)%4)
            
            case 5:
                check_cctv(x, y, select_num)
                check_cctv(x, y, (select_num+1)%4)
                check_cctv(x, y, (select_num+2)%4)
                check_cctv(x, y, (select_num+3)%4)

    count = 0
    for _office_checked_row in office_checked:
        for num in _office_checked_row:
            if (num == 0):
                count += 1

    min_count = min(min_count, count)

print(min_count)