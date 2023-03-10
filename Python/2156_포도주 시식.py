input = __import__("sys").stdin.readline

N = int(input())
arr = [0] * 10002
dp = [0] * 10002

for i in range(1, N+1):
    arr[i] = int(input())

dp[1] = arr[1]
dp[2] = dp[1] + arr[2]

for n in range(3, N+1):
    dp[n] = max(
        dp[n-3] + arr[n] + arr[n-1],
        dp[n-2] + arr[n],
        dp[n-1]
    )

print(dp[N])

# ----------------------------------

input = __import__("sys").stdin.readline

N = int(input())
arr = [0] * 10002
for i in range(N):
    arr[i] = int(input())

dp = [0] * 10002
dp[0] = arr[0]
dp[1] = dp[0] + arr[1]
dp[2] = max(
    arr[0] + arr[2], 
    arr[2] + arr[1], 
    dp[1]
)

for n in range(3, N):
    dp[n] = max(
        dp[n-2] + arr[n],
        dp[n-3] + arr[n] + arr[n-1],
        dp[n-1]
    )

print(dp[N-1])
