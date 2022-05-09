n, k = map(int, input().split())
ai = [int(input()) for _ in range(n)][::-1]  # 리스트 반전
count = 0

for a in ai:  # 큰 수 부터 반복
    i = k//a
    if i != 0:  # 몫이 0이 아니면,
        count += i  #count에 몫 더하기
        k -= i * a
print(count)