def step(array):

    end = len(array) - 1
    furtherest_step = 0
    
    for i in range(len(array)):
        if i <= furtherest_step:
            if furtherest_step < (i + array[i]):
                furtherest_step = (i + array[i])
        else:
            break
    
    if furtherest_step >= end:
        return True
    else:
        return False
        
def step2(array):
    furtherest_reached = 0
    end = len(array) - 1
    index = 0

    while index <= furtherest_reached and furtherest_reached < end:
        furtherest_reached = max(furtherest_reached, (index + array[index]))
        index += 1
    
    return furtherest_reached >= end

x = [3, 3, 1, 0, 2, 0, 1]
y = [3, 2, 0, 0, 2, 0, 1]

print(step2(y))