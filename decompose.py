def decompose(n):
    sum = 0
    x = n-1
    res = []
    while x > 0:
        if sum + x**2 <= n**2:
            sum += x**2
            res.append(x)
            if sum == n**2: return sorted(res)
        print (x, sum)
        x -= 1
    return None

print(decompose (50))
