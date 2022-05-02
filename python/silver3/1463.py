# 1로 만들기
dpdict = {1:0, 2:1, 3:1}

def calc(num):
    # dpdict에 num에 해당하는 값이 있으면 가져옴(반복 방지)
    if num in dpdict:
        return dpdict[num]

    # calc(3으로 나눈값)+ -1한 횟수, calc(2로 나눈값)+ -1한 횟수
    # 10의 경우 -> calc(10//3) + 1 -> ...
    count = min(calc(num//3)+num%3, calc(num//2)+num%2) + 1
    dpdict[num] = count
    return count

# 함수 구동
i = int(input())
print(calc(i))