# f(1)의 개수 == n번째 피보나치 수
# f(0)의 개수 == f(2)의 개수
# f(2)의 개수 == f(3)의 개수 + f(4)의 개수
# f(3)의 개수 == f(4)의 개수 + f(5)의 개수
# f(4)의 개수 == f(5)의 개수 + f(6)의 개수
# f(5)의 개수 == f(6)의 개수 + f(7)의 개수
# f(6)의 개수 == f(7)의 개수 + f(8)의 개수
# {7: 0, 6: 1, 5: 1, 4: 2, 3: 3, 2: 5}

import sys

def fibonacci_dp(n):
    if n == 0:
        dp[n] += 1
        return 0
    elif n == 1:
        dp[n] += 1
        return 1

    if n in dp:
        return dp[n]

    dp[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)

    return dp[n]

input()
num_list = map(int, sys.stdin.read().split())

for n in num_list:
    dp = {0: 0, 1: 0}
    one_count = fibonacci_dp(n)
    print(dp[list(dp.keys())[-2]], one_count)

for n in num_list:
    dp0 = [1, 0]
    dp1 = [0, 1]

    for i in range(2, n+1):
        dp0.append(dp0[i-1] + dp0[i-2])
        dp1.append(dp1[i-1] + dp1[i-2])

    print(dp0[n], dp1[n])
