def valid_parentheses(string):
    r = 0
    l = 0
    v = 0
    x = 0
    length = len(string)
    
    for i in string:
        v += 1
        if v == 1 and i == "(":
            x += 1
        elif v == length and i == ")":
            x += 1
            
        if i == ")":
            r += 1
        elif i == "(":
            l += 1

            
    if r == l and x == 2:
        return True
    else:
        return False

print(valid_parentheses("hi(hi)()"))
