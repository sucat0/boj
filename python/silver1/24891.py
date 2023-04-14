# 24891번: 단어 마방진

def check_mabang(input_list:list, size:int) -> bool:
    is_mabang = True
    for index in range(size):
        row_word = input_list[index]
        colnum_word = [input_list[colnum_index][index] for colnum_index in range(size)]
        if colnum_word != row_word:
            is_mabang = False
    
    return is_mabang

def sort_key(input_list:list) -> str:
    key = ''
    for word in input_list:
        key += ''.join(word)

    return key

def main():
    l, n = map(int, input().split())
    word_list = [list(input()) for _ in range(n)]

    has_mabang = False
    mabangs = []
    for index in range(n-l+1):
        sliced_word_list = word_list[index:index+l]
        is_mabang = check_mabang(sliced_word_list, l)
        if is_mabang:
            has_mabang = True
            mabangs.append(sliced_word_list)

    if has_mabang:
        mabangs.sort(key=sort_key)
        mabang = mabangs[0]
        for word in mabang:
            print(''.join(word))
    else:
        print('NONE')

main()