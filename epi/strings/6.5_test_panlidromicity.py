def test_palindromicity(string):
    forward  = 0
    backward = len(string) - 1

    while forward < backward:
        while not string[forward].isalnum() and forward < backward:
            forward += 1
        while not string[backward].isalnum() and forward < backward:
            backward -=1
        if string[forward].lower() != string[backward].lower():
            return False
        forward += 1
        backward -= 1

    return True

def test_palindromicity_2(string):
    forward = 0
    backward = len(string) - 1

    while forward < backward:
        while not string[forward].isalnum() and forward < backward:
            forward += 1
        while not string[backward].isalnum() and forward < backward:
            backward -= 1
        
        if string[forward].lower() != string[backward].lower():
            return False
        forward += 1
        backward -= 1
    return True

string = "A man, a plan, a canal, Panama"
string2 = 'ray a Ray'

print(test_palindromicity_2(string))
    