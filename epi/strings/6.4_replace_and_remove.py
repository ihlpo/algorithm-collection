def replace_a_remove_d(string): #O(n) time O(n) space
    final_string = []
    for i in string:
        if i == 'a':
            final_string.append('d')
            final_string.append('d')
            continue
        if i == 'b':
            continue
        final_string.append(i)
    return final_string

def replace_a_remove_d_2(string): #O(n) time O(n) space
    final_string = string.replace("a", "dd")
    final_string = final_string.replace("b","")

    return final_string


x = 'acdbbca'

print(replace_a_remove_d_2(x))