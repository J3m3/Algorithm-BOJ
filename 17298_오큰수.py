import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
result = [-1] * n
stack = []

for idx in range(n-1):
    stack.append(idx)
    while nums[stack[-1]] < nums[idx+1]:
        result[stack.pop()] = nums[idx+1]
        if not stack:
            break

print(*result)