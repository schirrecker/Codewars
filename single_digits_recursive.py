def single_digit(n):
    r = 0
    b_str = bin(n)[2:]
    for c in b_str:
        r += int(c)

    if r < 10:
        return r
    else:
        return single_digit(r)


print(single_digit(5665))
