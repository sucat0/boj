n = int(input())  # 사람의 수 N
p = list(map(int, input().split()))  # 인출시간 입력->스페이스바 나누기->리스트 요소 int 형변환

p = sorted(p)  # p배열 정렬
s = 0
for i in range(n):
    s += sum(p[:i+1])  # p배열 처음부터 i+1인덱스까지 슬라이상->값 전부 더함->결과값에 더함
print(s)