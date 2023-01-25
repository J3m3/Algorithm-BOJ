import sys
stack_L = list(sys.stdin.readline().rstrip())
stack_R = []
input()
commands = sys.stdin.read().rstrip().split('\n')

for command in commands:
    if command[0] == 'L':
        if stack_L:
            stack_R.append(stack_L.pop())

    elif command[0] == 'D':
        if stack_R:
            stack_L.append(stack_R.pop())

    elif command[0] == 'B':
        if stack_L:
            stack_L.pop()

    else:
        stack_L.append(command[-1])

print(''.join(stack_L + stack_R[::-1]))