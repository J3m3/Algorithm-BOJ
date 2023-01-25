input = __import__("sys").stdin.readline

N = int(input())
meeting_list = []

for _ in range(N):
    s, e, p = map(int, input().split())
    meeting_list.append((s, e, p))
meeting_list.sort(key=lambda x: (x[0], x[1]))

dp = [0] * N
dp[0] = meeting_list[0][2]

if N == 1:
    result = dp[0]
else:
    dp[1] = max(dp[0], meeting_list[1][2])

    for i in range(2, N):
        dp[i] = max(
            meeting_list[i][2] + dp[i-2],
            dp[i-1]
        )
    result = dp[N-1]

print(result)