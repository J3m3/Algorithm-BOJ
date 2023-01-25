import sys

input()
nums = list(map(int, sys.stdin.read().split()))
commands = []
stack = []
start = 0

for num in nums:
    if num in stack: # in의 시간 복잡도가 O(n)이라 시간 초과난 듯.
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