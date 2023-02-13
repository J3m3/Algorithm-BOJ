input = __import__("sys").stdin.readline

N = int(input())

a, b = 1, 3
if N & 1:
    print(0)
else:
    for i in range(0, N, 2):
        b, a = 4 * b - a, b
    print(a)

# -------------------------------------

'''With DP table'''
input = __import__("sys").stdin.readline

N = int(input())

if N & 1:
    print(0)
else:
    dp = [0] * ((N >> 1) + 1)
    dp[0] = 1
    dp[1] = 3
    for i in range(2, (N >> 1) + 1):
        dp[i] = 4 * dp[i-1] - dp[i-2]

    print(dp[-1])

# -------------------------------------

'''More detailed version'''
input = __import__("sys").stdin.readline

N = int(input())

if N & 1:
    print(0)
else:
    dp = [0] * ((N >> 1) + 1)
    dp[0] = 1
    dp[1] = 3
    for i in range(2, (N >> 1) + 1):
        dp[i] = 3 * dp[i-1]
        for j in range(i-1):
            dp[i] += 2 * dp[j]

    print(dp[-1])
