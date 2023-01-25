# input = __import__("sys").stdin.readline

# dp = [0] * 12
# dp[1], dp[2], dp[3] = 1, 2, 4
# for i in range(4, 12):
#     dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

# for _ in range(int(input())):
#     print(dp[int(input())])

# ------------------

input = __import__("sys").stdin.readline

def dfs(total, target):
    if total == target:
        global count
        count += 1
        return
    
    for i in range(1, 4):
        total += i
        if total <= target:
            dfs(total, target)
            total -= i

for _ in range(int(input())):
    count = 0
    dfs(0, int(input()))
    print(count)