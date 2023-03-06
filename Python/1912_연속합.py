input = __import__("sys").stdin.readline

N = int(input())
arr = list(map(int, input().split()))

maximum = arr[0]
dp = [0] * (N+1)
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    maximum = max(dp[i], maximum)

print(maximum)
