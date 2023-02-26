input = __import__("sys").stdin.readline

N = int(input())
T = [0]
P = [0]
dp = [0] * (N+60)

for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
    dp[i + 1] = max(dp[i], dp[i+1])

print(dp[N+1])

'''
dp[n] == n일에 벌 수 있는 최대 금액

어떤 위치의 최대값을 갱신할 때에는...
1. 오늘 일을 하거나 => "더 큰 오늘의 P 값을 더해주면 됨"
2. 오늘 일을 안 하거나 => "더 큰 미래의 P 값을 유지하면 됨"

다만...
중간에 건너뛰어진 부분은 0으로 고정되는 문제가 있기 때문에,
항상 직전까지의 최대값을 가져와서 update해야 함
'''