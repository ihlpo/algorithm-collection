def add(array):
    array[-1] += 1
    for i in reversed(range(1, len(array))):
        if array[i] == 10:
            array[i] = 0
            array[i - 1] += 1
    if array[0] == 10:
        array[0] = 1
        array.append(0)

    return array

x = [9,9,9]
print(add(x))