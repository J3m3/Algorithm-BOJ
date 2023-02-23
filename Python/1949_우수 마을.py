import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(this):
    visited[this] = 1
    for child in tree[this]:
        if not visited[child]:
            dfs(child)

            dp[this][1] += dp[child][0]
            dp[this][0] += max(dp[child][0], dp[child][1])

N = int(input())
visited = [0] * (N+1)
dp = [[0] * 2 for _ in range(N+1)]
tree = [[] for _ in range(N+1)]

for i, p in enumerate(map(int, input().split())):
    dp[i+1][1] = p

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(max(dp[1][0], dp[1][1]))