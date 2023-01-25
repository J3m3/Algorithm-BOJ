import sys

n = int(sys.stdin.readline())

dic = [0] * 1000001
nums = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    dic[nums[i]] += 1

stack = []
result = [-1] * n
for idx in range(n):
    while stack and dic[nums[stack[-1]]] < dic[nums[idx]]:
        result[stack.pop()] = nums[idx]

    stack.append(idx)

print(*result)
