import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(cur):
    visited[cur] = 1
    for child in tree[cur]:
        if not visited[child]:
            dfs(child)

            dp[cur][0] += dp[child][1]
            dp[cur][1] += min(dp[child][0], dp[child][1])

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [0] * (N+1)
dp = [[0, 1] for _ in range(N+1)]

dfs(1)

print(min(dp[1][0], dp[1][1]))
