def delete_duplicates(array):
    length = len(array)
    lookup_dict = {}
    
    for i in array:
        if i in lookup_dict:
            continue
        lookup_dict[i] = i

    return_array = [y for x,y in lookup_dict.items()]

    return(len(lookup_dict))

    while len(return_array) <= length:
        return_array.append(0)
    
    return return_array



def delete_duplicates2(array):
    count = 1
    
    for i in range (1, len(array)):
        if array[i] != array[i-1]:
            count += 1

    return count

def delete_duplicates3(array):
    count = 1 

    for i in range(1, len(array)):
        if array[count - 1] != array[i]:
            array[count] = array[i]
            count += 1
    return count

x = [2, 3, 5, 5, 7, 11, 11, 13]
y = [2, 2, 2, 2]
print(delete_duplicates3(y))
