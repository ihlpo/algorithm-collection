import random

def random_sampling(array, size):
    for i in range(size):
        random_index = random.randint(i, len(array) - 1)
        array[i], array[random_index] = array[random_index], array[i]
    return array[:size]

x = [3,7,5,1]
print(random_sampling(x,3))