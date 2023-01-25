from collections import deque
input = __import__("sys").stdin.readline

def BFS(graph, start, order):
    queue = deque([start])
    while queue:
        this = queue.popleft()
        for child in graph[this]:
            if orders[child] == 0:
                queue.append(child)
                orders[child] = order
                order += 1


V, E, S = map(int, input().split())
graph = {v:[] for v in range(1, V+1)}
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in graph:
    graph[v].sort(reverse=True)

orders = [0] * (V+1); orders[S] = 1

BFS(graph, S, 2)

for v in range(1, V+1):
    print(orders[v])