input = __import__("sys").stdin.readline

N = int(input())
H = [0]
for _ in range(N):
    H.append(int(input()))

result = 0
stack = []
for i in range(1, N + 1):
    while stack and H[stack[-1]] <= H[i]:
        stack.pop()
    result += len(stack)
    stack.append(i)

print(result)
