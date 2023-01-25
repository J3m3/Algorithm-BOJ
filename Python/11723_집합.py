from sys import stdin

bit_set = 0
for _ in range(int(stdin.readline())):
    commands = stdin.readline().split()

    if commands[0] == "all":
        bit_set = (1 << 20) - 1
    
    elif commands[0] == "empty":
        bit_set = 0
    
    else:
        num = int(commands[1]) - 1

        if commands[0] == "add":
            bit_set = bit_set | (1 << num)
        
        elif commands[0] == "check":
            print(0 if (bit_set & (1 << num)) == 0 else 1)
        
        elif commands[0] == "toggle":
            bit_set = bit_set ^ (1 << num)
        
        elif commands[0] == "remove":
            bit_set = bit_set & ~(1 << num)