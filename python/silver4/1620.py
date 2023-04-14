from sys import stdin

n, m = map(int, stdin.readline().split())

name_dict = {}
index_dict = {}
for index in range(1, n+1):
    name = stdin.readline().strip()
    name_dict[name] = index
    index_dict[index] = name

for _ in range(m):
    question = stdin.readline().strip()
    is_int = question.isdigit()

    if is_int:
        question = int(question)
        print(index_dict[question])

    else:
        print(name_dict[question])