from collections import deque
input = __import__("sys").stdin.readline
INF = float('inf')

N = int(input())
dp = [INF] * (1000002)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    dp[i] = dp[i-1]
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2])
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3])

    dp[i] += 1

print(dp[N])

queue = deque([N])
visited = [False] * (N+1)
result = [N]
while queue:
    cur = queue.popleft()

    if cur == 1:
        break

    child = cur - 1
    minimum = dp[cur - 1]
    if cur % 2 == 0 and minimum > dp[cur // 2]:
        minimum = dp[cur // 2]
        child = cur // 2

    if cur % 3 == 0 and minimum > dp[cur // 3]:
        minimum = dp[cur // 3]
        child = cur // 3

    queue.append(child)
    result.append(child)

print(*result)
