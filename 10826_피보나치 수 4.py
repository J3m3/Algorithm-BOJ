dp = {}
def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n in dp:
        return dp[n]

    dp[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)

    return dp[n]

a, b = 0, 1
for _ in range(int(input())):
    a, b = b, a + b

print(a)