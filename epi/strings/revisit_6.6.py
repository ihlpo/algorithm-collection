def reverse_words(string): #O(n) time O(n) space
    reverse_string = list(reversed(list(string)))

    def reverse_word(string_array, start, end):
        i = 0
        j = len(string_array) - 1

        while i < j:
            string_array[i], string_array[j] = string_array[j], string_array[i]
            i += 1
            j -= 1
        reverse_string[start:end] = string_array

    start_word = 0
    for end_word in range(len(string)):
        if reverse_string[end_word] == " ":
            reverse_word(reverse_string[start_word:end_word], start_word, end_word)
            start_word = end_word + 1
    
    reverse_word(reverse_string[start_word:len(reverse_string)], start_word, len(reverse_string))
    
    return "".join(reverse_string)

x = 'ram is costly'

print(reverse_words(x))