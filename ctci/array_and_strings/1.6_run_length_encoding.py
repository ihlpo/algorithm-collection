def compress_string(string):
    """
    Run-length Encoding
    O(n) Time O(n) Space. To compress the string, we need to keep a count of
    duplicate chars in a sequence. We can use 2 pointers where one pointer keeps
    moving until it finds a distinct character while adding the count. Once found
    we insert the formated character in a list and move on. The current pointer
    takes the location of the new distinct location and the distinct pointer
    moves one step."""
    compressed_chars = []
    current_char = 0 
    distinct_char = 1
    
    while current_char < len(string):
        count = 1
        while distinct_char < len(string) and string[distinct_char] == string[current_char]:
            duplicates = True
            count += 1
            distinct_char += 1

        compressed_chars.append(f'{string[current_char]}{count}') # f-strings
        current_char = distinct_char #Current Char becomes next distinct char
        distinct_char += 1 #Distinct moves 1 over to check against current char
    
    return ''.join(compressed_chars)

x ='aaaaddbbbcd'

print(compress_string(x))