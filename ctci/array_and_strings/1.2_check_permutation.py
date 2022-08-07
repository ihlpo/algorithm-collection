def check_permutation(string1, string2):
    """O(n) time O(n) space. Uses a dictionary to keep count of the characters"""
    if len(string1) != len(string2):
        return False

    char_counts = {}

    for i in string1:
        if i not in char_counts:
            char_counts[i] = 1
        else:
            char_counts[i] += 1

    for j in string2:
        if j in char_counts:
            char_counts[j] -= 1
    
    for i, j in char_counts.items():
        if j > 0:
            return False
    return True

def check_permutation2(string1, string2):
    """O(nlogn) time from sorting the strings and O(n) space from sorted() returning a new copy."""
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)

    return True if sorted1 == sorted2 else False

x = 'cbaaaa'
y = 'abcaaa'

print(check_permutation(x,y))