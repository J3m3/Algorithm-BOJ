import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(node, total):
    visited[node] = True
    for w, v in tree[node]:
        if not visited[v]:
            global max_cost, end_node
            
            cur_cost = total + w
            if cur_cost > max_cost:
                max_cost = cur_cost
                end_node = v

            dfs(v, cur_cost)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u].append((w, v))
    tree[v].append((w, u))

end_node = 0
max_cost = 0

visited = [False] * (N+1)
dfs(1, 0)

visited = [False] * (N+1)
dfs(end_node, 0)

print(max_cost)