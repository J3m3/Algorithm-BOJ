'''
1 -> 0
2 -> 1
3 -> 1
4 -> min(dp[4//2], dp[4-1])
5 -> dp[5-1]
6 -> min(dp[6//2], dp[6//3], dp[6-1])
'''

input = __import__("sys").stdin.readline

N = int(input())
dp = [0, 0, 1, 1] + [1] * (N - 3)

for i in range(4, N+1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] += min(dp[i//2], dp[i//3], dp[i-1])
    
    elif i % 2 == 0:
        dp[i] += min(dp[i//2], dp[i-1])
    
    elif i % 3 == 0:
        dp[i] += min(dp[i//3], dp[i-1])

    else:
        dp[i] += dp[i-1]

print(dp[N])