result = ""
count = 0
temp_word = ""

for c in input()+' ':
    if c == '<':
        result += temp_word[::-1]
        temp_word = ""
        count += 1

    if count >= 1:
        result += c
    else:
        if c == ' ':
            result += temp_word[::-1] + ' '
            temp_word = ""
        else:
            temp_word += c
    
    if c == '>':
        count -= 1

print(result)