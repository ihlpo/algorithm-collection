# check if a string is a panlindrom

def is_panlindrom(string): #O(n) Time O(n) Space
    reversed_string = "".join(list(reversed(string)))
    return string == reversed_string

def is_panlindrom2(string): #O(n) Time O(1) Space
    forward = 0
    backward = len(string) - 1
    
    while forward != backward:
        if string[forward] != string[backward]:
            return False
        else:
            forward += 1
            backward -= 1
    return True

x = "aaba"

print(is_panlindrom(x))