input = __import__("sys").stdin.readline

N = int(input())
if N < 3:
    result = 1 if N == 1 else 2
else:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    for i in range(4, N+1):
        dp[i] = min(dp[i-1], dp[i-3]) + 1
    
    result = dp[N]

print(["SK", "CY"][result & 1])