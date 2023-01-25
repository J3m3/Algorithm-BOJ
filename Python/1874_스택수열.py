import sys

input()
nums = map(int, sys.stdin.read().split())
commands = []
stack = []
start = 1

for num in nums:
    for i in range(start, num+1):
        stack.append(i)
        commands.append("+")
        start += 1

    if num == stack[-1]:
        stack.pop()
        commands.append("-")
    else:
        print("NO")
        break

else:
    print('/n'.join(commands))