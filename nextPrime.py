def isPrime(n):
    prime = True
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            prime = False
    return prime
        
    
def nextPrime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    for i in range(n+1, n*2):
        if isPrime(i):
            return i


print(nextPrime(3))
print(isPrime(4))
