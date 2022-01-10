def amidakuji(ar):

    horz = len(ar[0])
    vert = len(ar)
    res = [0] * horz
 
    for x in range(0, horz):
        pos = 0
        for y in range(0, vert):
            if x + pos < horz and ar[y][x+pos] == '1':
                pos += 1
                print ("+1", "pos=", pos, " x+pos=:", x+pos, " y=", y)
            elif x + pos > 0 and ar[y][x+pos-1] == '1':
                pos -= 1
                print ("-1", "pos=", pos, " x+pos=:", x+pos, " y=", y)
        res[x+pos-1] = x
    return res


ar = [		'000001',
		'010010',
		'101001',
		'010100',
		'001010',
		'010000',
		'100010',
		'010100']

print(amidakuji(ar))

