def is_one_edit_away(string1, string2):
    """
    O(n+m) time while n m are length the strings respectively. O(1) space.
    The difference of length in both strings cannot be greater than 1
    because we can testing if its 1 edit away. Some intuition... We can keep a count of how many
    edits needs for the strings to be the same. Each operation: insert, delete, or replace will
    increase the count by one. We can iterate both strings at the same time using AND condition to
    make sure the strings will not go out of bound and check whether the characters are the same.
    We will handle the cases where the length of each string is not the same.  
    if not, 1 edit is needed. if the edit count is greater than 2 we can 
    return false. we handle the insert and delete operations by incrementing the longer string by 1 when the 
    charcters are not the same. If the length of the charaters are the same but the characters are different
    we can assume a replace operation will take place. Increasing the edit count by 1 and incrementing both 
    indexes. When the initial loop is broken, we handle the longer string's last character by incrementing
    the edit count assuming its a delete. Finally, we check whether the edit count is greater than 1. If so,
    return False else True.
    """
    edit_count = 0
    length_of_string1 = len(string1)
    length_of_string2 = len(string2)
    i = 0
    j = 0

    if abs(length_of_string1 - length_of_string2) > 1:
        return False

    while i < length_of_string1 and j < length_of_string2:
        if string1[i] != string2[j]:
            if edit_count > 1:
                return False
            edit_count += 1
            if length_of_string1 > length_of_string2:
                i += 1
            elif length_of_string2 > length_of_string1:
                j += 1
            else: #Strings are the same length
                i += 1
                j += 1
        else: #Charaters are equal
            i += 1
            j += 1

    if i < length_of_string1 or j < length_of_string2: #Handles the last character of the longer string
        edit_count += 1
    
    return edit_count < 2

x = ['pale', 'pales', 'pale', 'pale']
y = ['ple', 'pale', 'bale', 'bake']

for i , j in enumerate(range(len(x))):
    print(is_one_edit_away(x[i],y[j]))


        
        
        