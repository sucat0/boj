def check_fit(laptop, sticker, laptop_part, row_start, col_start):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1 and laptop_part[i][j] == 1:
                return 0
            
    sticker_sum = 0
            
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                laptop[i+row_start][j+col_start] = 1
                sticker_sum += 1
    
    return sticker_sum

def laptop_part(laptop, row_start, row_end, col_start, col_end):
    part = []
    for i in range(row_start, row_end):
        part_row = []
        for j in range(col_start, col_end):
            part_row.append(laptop[i][j])
        
        part.append(part_row)

    return part

def check_non_rotate(laptop, sticker):
    for i in range(len(laptop)-len(sticker) + 1):
        for j in range(len(laptop[0])-len(sticker[0]) + 1):
            part = laptop_part(laptop, i, i+len(sticker), j, j+len(sticker[0]))
            sticker_sum = check_fit(laptop, sticker, part, i, j)
            if sticker_sum != 0:
                return sticker_sum
            
    return 0

def rotate(sticker):
    new_sticker = []
    for i in range(len(sticker[0])):
        new_row = []
        for j in reversed(range(len(sticker))):
            new_row.append(sticker[j][i])
        new_sticker.append(new_row)
    
    return new_sticker

def check_all(laptop, sticker):
    cur_sticker = sticker
    for _ in range(4):
        if len(laptop) < len(cur_sticker) or len(laptop[0]) < len(cur_sticker[0]):
            cur_sticker = rotate(cur_sticker)
            continue

        sticker_sum = check_non_rotate(laptop, cur_sticker)

        if sticker_sum != 0:
            return sticker_sum
    
        cur_sticker = rotate(cur_sticker)

    return 0

def main():
    n, m, k = map(int, input().split())

    laptop = [[0 for _ in range(m)] for _ in range(n)]
    sticker_sum = 0

    for i in range(k):
        r, c = map(int, input().split())

        sticker = []
        for _ in range(r):
            sticker.append(list(map(int, input().split())))

        sticker_sum += check_all(laptop, sticker)

    print(sticker_sum)

if __name__ == "__main__":
    main()
    