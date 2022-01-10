def uniq(l):
    l1 = l[:]
    for i in l1:
        if l1.count(i) == 1:
            return i
        else:
            l1 = [x for x in l1 if x != i]

l = [1, 1, 1, 2, 1, 1, 1]

print(uniq(l))
