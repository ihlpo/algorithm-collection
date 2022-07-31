def look_say(n): #O(n(2^n))
    def get_next(sequence):
        result = []
        index = 0
        while index < len(sequence):
            count = 1
            while index + 1 < len(sequence) and sequence[index] == sequence[index + 1]:
                index += 1
                count += 1
            result.append(str(count) + sequence[index])
            index += 1
        return ''.join(result)
    

    number = '1'    
    for _ in range(1, n):
        number = get_next(number)
        print(number)

    return number

print(look_say(8))