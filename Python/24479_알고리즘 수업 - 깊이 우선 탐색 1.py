import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def DFS(graph, start):
    global order
    for child in graph[start]:
        if orders[child] == 0:
            orders[child] = order
            order += 1
            DFS(graph, child)

V, E, S = map(int, input().split())

graph = {v: [] for v in range(1, V+1)}
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in graph:
    graph[v].sort()

order = 2
orders = [0] * (V+1); orders[S] = 1
DFS(graph, S)

for v in range(1, V+1):
    print(orders[v])