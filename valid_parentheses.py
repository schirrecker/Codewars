import itertools

def valid_parentheses(s):
    open_list = []
    for p in s:
            if p == ")":
                    if open_list == []:
                            return False
                    else:
                            open_list.pop()
            else:
                    open_list.append(p)
    return len(open_list) == 0

# test valid_parentheses function
# s = ")()"
# print(valid_parentheses(s))

def flip_parentheses(s, n):
    combinations = []
    l = [i for i in range(len(s))]
    for flip in itertools.combinations(l, n):
            # print (flip)
            s_list = list(s)
            for i in flip:
                    if s_list[i] == ")":
                            s_list[i] = "("
                    else:
                            s_list[i] = ")"
            combinations.append(''.join(s_list))
    # print(combinations)
    return combinations
    
def solve(s):
    for n in range(1, len(s)+1):
        # print("changing " + str(n))
        for flip_string in flip_parentheses(s, n):
            if valid_parentheses(flip_string):
                return n
            return (-1)
    

print(solve(")()("),2)
print(solve("((()"),1)
print(solve("((("),-1)
print(solve("())((("),3)
print(solve("())()))))()()("),4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
