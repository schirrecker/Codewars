def single_digit(n):
    n = sum(int(digit) for digit in str(int(bin(n)[2:])))
    while n > 9:
        n = sum(int(digit) for digit in str(int(bin(n)[2:])))
    return n

print(single_digit(123456789))

