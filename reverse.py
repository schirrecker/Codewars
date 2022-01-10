def solve(s):
    spaces = []
    i = 0
    for c in s:
        if c == " ":
            spaces.append(i)
        i += 1
    print(spaces)
    s_reverse = s[::-1]
    s_reverse = s_reverse.replace(" ", "")
    print(s_reverse)
    for i in spaces:
        s_reverse = s_reverse[:i] + ' ' + s_reverse[i:]
    print(s_reverse)
    return s_reverse
    


solve ("your code")
solve ("your code rocks")
