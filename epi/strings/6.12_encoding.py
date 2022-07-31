def encode(string):
    encode_list = []
    count = 1

    for i in range(1, len(string) + 1):
        if i == len(string) or string[i] != string[i - 1]:
            encode_list.append(str(count) + string[i - 1])
            count = 1

        else:
            count += 1
    return "".join(encode_list)

def decode(string):
    decode_list = []
    count_list = []

    for i in string:
        if i.isdigit():
            count_list.append(i)
        else:
            count = int("".join(count_list))
            character = i * count
            decode_list.append(character)
            count_list.clear()
    return "".join(decode_list)


x = "aaaabcccaa"
y = "10e4f12c"
print(decode(y))

