from sys import stdin

l = int(stdin.readline())
word = stdin.readline()

word_hash = 0
for index in range(l):
    ascii = ord(word[index])
    word_hash += (ascii-96) * (31 ** index)

word_hash %= 1234567891

print(word_hash)