def snake_string(string):
    return string[1::4] + string[::2] + string[3::4]
    
x = "Hello World!"

print(snake_string(x))