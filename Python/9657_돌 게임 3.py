input = __import__("sys").stdin.readline

N = int(input())

'''
1개 - 1
2개 - 2
3개 - 1
4개 - 1
5개 - dp[4], dp[2], dp[1] (상근이가 3개 가져가면 됨)
6개 - dp[5], dp[3], dp[2] (상근이가 4개 가져가면 됨)
7개 - dp[6], dp[4], dp[3]
'''

dp = [1] * 1002
dp[2] = 2
for i in range(5, N+1):
    for j in [i-1, i-3, i-4]:
        if dp[j] & 1:
            continue
        dp[i] = dp[j]
        break
    dp[i] += 1

print(["CY", "SK"][dp[N] & 1])
