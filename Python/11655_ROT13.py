UP_START = ord('A')
UP_END = ord('Z')
LOW_START = ord('a')
LOW_END = ord('z')

for char in input():
    if char.isupper():
        ascii = (ord(char) + 13 - UP_START) % (UP_END - UP_START + 1) + UP_START
        print(chr(ascii), end='')
    
    elif char.islower():
        ascii = (ord(char) + 13 - LOW_START) % (LOW_END - LOW_START + 1) + LOW_START
        print(chr(ascii), end='')
    
    else:
        print(char, end='')