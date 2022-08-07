def palindrom_permutation(string):
    """O(n) time O(n) space"""
    total_characters = len(string.replace(' ',''))
    char_counts = {}
    for i in string: #Builds a dictionary of character counts. Skipping spaces.
        if i.isalpha():
            if i in char_counts:
                char_counts[i] += 1
            else:
                char_counts[i] = 1

    if total_characters % 2 != 0:
        seen_single_char = False
        for k,v in char_counts.items():
            if v % 2 != 0:
                if seen_single_char == True:
                    return False
                else:
                    seen_single_char = True   
        return True
        
    else:
        for k,v in char_counts.items():
            if v % 2 != 0:
                return False 
        return True

def palindrom_permutation2(string):
    """O(n) time O(n) space. To be a panlindrome, The number of odd characters can only be less or equal to 1"""
    char_counts = {}
    for i in string: #Builds a dictionary of character counts. Skipping spaces.
        if i.isalpha():
            if i in char_counts:
                char_counts[i] += 1
            else:
                char_counts[i] = 1

    total_odd_counts = [1 for v in char_counts.values() if v % 2 != 0] #Gathers all characters with odd counts.
    
    return sum(total_odd_counts) <= 1