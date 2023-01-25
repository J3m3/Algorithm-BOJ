import sys

seq = list(sys.stdin.readline().rstrip())

stack = []
result = []
priority_map = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1}

for char in seq:
    if char.isalpha():
        result.append(char)

    elif char == '(':
        stack.append(char)

    elif char == ')':
        while stack[-1] != '(':
            result.append(stack.pop())

        stack.pop()

    else:
        while stack and priority_map[stack[-1]] >= priority_map[char]:
            result.append(stack.pop())

        stack.append(char)

while stack:
    result.append(stack.pop())

print("".join(result))