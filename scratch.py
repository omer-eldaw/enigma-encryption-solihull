def print_formatted(number):
    for i in range(1, number):
        octal_rep = oct(i)
        octal_rept = 
        hexadecimal_rep = hex(i)
        hexadecimal_rep = "0x{value:hex}"
        binary_rep = bin(i)
        length_of_biary_rep = int(len(binary_rep))
        print(f'{i:>5} {octal_rep:>5} {hexadecimal_rep:>5} {binary_rep:>5}')




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)