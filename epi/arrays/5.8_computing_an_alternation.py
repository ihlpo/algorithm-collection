def make_alternation(array):
    for i in range(len(array) - 1):
        if i % 2 == 0 and array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        elif i % 2 != 0 and array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    return array


x = [1,5,2,8,15,6,9]
print(rearrange(x))