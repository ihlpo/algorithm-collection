def national_flag(array, index):
    array1 = []
    for i in array:
        if i < array[index]:
            array1.append(i)

    for i in array:
        if i == array[index]:
            array1.append(i)

    for i in array:
        if i > array[index]:
            array1.append(i)

    return array1

def national_flag2(array, index):
    pivot = array[index]

    smaller = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smaller] = array[smaller], array[i]
            smaller += 1
    larger = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break
        elif array[i] > pivot:
            array[i], array[larger] = array[larger], array[i]
            larger -=1

    return array
    
def national_flag3(array, index):
    pivot = array[index]
    
    smallp = 0
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[smallp] = array[smallp], array[i]
            smallp += 1

    large = len(array) - 1
    for i in reversed(range(len(array))):
        if array[i] < pivot:
            break
        if array[i] > pivot:
            array[i], array[large] = array[large], array[i]
            large -= 1

x = [3,3,2,4,5,1]

print(national_flag2(x, 3))