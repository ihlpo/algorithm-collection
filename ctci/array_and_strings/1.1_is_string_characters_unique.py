def unique_charaters(string): #O(n) O(n). Use a dictionary
    seen = {}

    for char in string:
        if char in seen:
            return False
        seen[char] = 0
    
    return True


def unique_charaters2(string):#O(nlogn) O(n). This does not use any data structures. sorted() return new list
    sorted_string = sorted(string)
    for i in range(1, len(string)):
        if sorted_string[i] == sorted_string[i-1]:
            return False

    return True

def unique_charaters3(string): #O(n2) O(1). This solution does not require extra space with a time tradeoff
    for i in range(len(string)):
        for j in range(len(string)):
            if i == j:
                continue
            if string[i] == string[j]:
                return False
    return True
