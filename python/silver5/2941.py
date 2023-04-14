from sys import stdin

word = list(stdin.readline())

length = len(word)
croatia = ('c=','c-','dz','d-','lj','nj','s=','z=')
word_count = 0
index = 0
while index != length-1:
    front_alphabet = word[index]
    back_alphabet = word[index+1]
    two_alphabet = front_alphabet+back_alphabet

    if two_alphabet in croatia:
        if two_alphabet == 'dz':
            if word[index+2] == '=':
                index += 2
        else:
            index += 1

    word_count += 1
    index += 1

print(word_count)