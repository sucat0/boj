# 1316번 그룹 단어 제거

from sys import stdin

n = int(stdin.readline())

group_count = 0
for _ in range(n):
    word = stdin.readline()

    alphabet_list = []
    alphabet_buff = ''
    is_group = True
    for index in range(len(word)):
        alphabet = word[index]
        if alphabet != alphabet_buff:
            if word[index] in alphabet_list:
                is_group = False
                break

            else:
                alphabet_list.append(alphabet)

        alphabet_buff = alphabet

    if is_group:
        group_count += 1

print(group_count)