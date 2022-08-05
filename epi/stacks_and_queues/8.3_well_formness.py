def well_formness(string): #O(n) O(n) #accounts for all other characters
    stack = []
    left = {
            "(": 0,
            "[": 0,
            "{": 0
            }

    for i in string:
        if i in left:
            stack.append(i)
        else:
            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()

            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
    return len(stack) == 0 

def well_formness2(string): #O(n) O(n) // Does not account for other characters in string 
    stack = []
    lookup = {
             '(': ')', 
            '{': '}',
            '[': ']'
             }

    for char in string:
        if char in lookup:
            stack.append(char)
        elif len(stack) == 0 or lookup[stack.pop()] != char:
            return False

    return len(stack) == 0