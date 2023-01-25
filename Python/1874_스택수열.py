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

# ----------------------------

import sys

input()
nums = list(map(int, sys.stdin.read().split()))
commands = []
stack = []
start = 0

for num in nums:
    if num in stack: # in의 시간 복잡도가 O(n)이기 때문에 TLE
        if num == stack[-1]:
            stack.pop()
            commands.append("-")
        else:
            print("NO")
            break
    else:
        for i in range(start+1, num+1):
            stack.append(i)
            commands.append("+")

        stack.pop()
        commands.append("-")
        
        start = num
else:
    for c in commands:
        print(c)