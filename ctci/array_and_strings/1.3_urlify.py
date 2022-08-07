def urlify(string):
    """O(n) time O(n) space. We need to create a new string because Python strings are immutable."""
    stripped_string = string.strip()
    return_list = []
    for i in stripped_string:
        return_list.append('%20') if i == ' ' else return_list.append(i) 
    
    return ''.join(return_list)

def urlify2(string):
    """O(n+m) time from the replace function. O(n) space. Both functions returns a copy of the original string."""
    stripped_string = string.strip()
    return stripped_string.replace(' ', '%20')

x = 'Mr John Smith     '
print(urlify2(x))