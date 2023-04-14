class Converter:
    @staticmethod
    def conv_to_num(str_num:str) -> list:
        num = []
        for str_bit in list(str_num):
            ascii_num = ord(str_bit)
            if ascii_num >= 65:
                num.append(ascii_num-55)  # A: 65(ascii) -> 36진수에서는 10 -> 65-10=55
            else:
                num.append(ascii_num-48)  # 0: 48(ascii) -> 36진수에서는 0 -> 48-0=48

        return reversed(num)  # 연산 편의성을 위해 뒤집음

    @staticmethod
    def conv_to_base36(dec_num:int) -> str:
        base36_num = ''
        while dec_num > 0:
            base36_bit = dec_num % 36
            ascii_num = base36_bit + 48 if base36_bit <= 9 else base36_bit + 55
            base36_num = chr(ascii_num) + base36_num
            dec_num //= 36

        return base36_num

def main():
    n = int(input())
    num_list = [Converter.conv_to_num(input()) for _ in range(n)]
    k = int(input())
    num_count = [[i, 0] for i in range(36)]

    for num in num_list:
        bit_index = 0
        for bit in num:
            num_count[bit][1] += (36 ** bit_index)
            bit_index += 1

    num_count.sort(key=lambda x: -(x[1]*35 - x[0]*x[1]))

    change_count = 0
    dec_sum = 0
    for num_index in range(36):
        bit = num_count[num_index][0]
        count = num_count[num_index][1]
        if change_count < k and count != 0:
            bit = 35
            change_count += 1
        dec_sum += bit * count

    if dec_sum == 0:
        result = '0'  # 망할 반례;;;;;;;;;;;;
    else:
        result = Converter.conv_to_base36(dec_sum)
    print(result)

if __name__ == "__main__":
    main()