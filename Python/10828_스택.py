import sys

input()
stack = []
for command in [c.split() for c in sys.stdin.read().rstrip().split('\n')]:
    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    elif command[0] == "size":
        print(len(stack))
    
    elif command[0] == "empty":
        print(int(not bool(stack)))

    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)