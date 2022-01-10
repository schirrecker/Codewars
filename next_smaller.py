

from itertools import permutations
def next_smaller(n):
    def convert(l):
        s = [str(i) for i in l] 
        return int("".join(s))  

    l = [int(x) for x in str(n)]
    perms = [convert(s) for s in permutations(l)]
    return min(perms, key=lambda x:x-n)

print(next_smaller(1234567998))
