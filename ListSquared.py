import math
def squared_divisors(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i*i
    sum += n*n
    return sum

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False



def list_squared(m, n):
    l = []
    for i in range(m,n):
        s = squared_divisors(i)
        if is_square(s):
            l.append([i,s])
    return l
            
print(list_squared(1346,35467))
