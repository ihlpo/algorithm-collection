def permutation(array, permuation):
    return_array = [0] * len(array)

    for i in range(len(array)):
        # perm = permuation[i]
        # current = array[i]
        return_array[permuation[i]] = array[i]

    return return_array

def permutation2(array, permuation):
    for i in range(len(array)):
        perm_pointer = i
        while permuation[perm_pointer] >= 0:
            array[i], array[permuation[perm_pointer]] = array[permuation[perm_pointer]], array [i]
            temp = permuation[perm_pointer]
            permuation[perm_pointer] -= len(array)
            perm_pointer = temp
    return array

   
x = [1,2,3,4,5,6]
y = [0,4,3,1,2,5]

print(permutation2(x,y))