input = __import__("sys").stdin.readline
INF = float('inf')

V, E = map(int, input().split())

graph = {v:[] for v in range(1, V+1)}
distance = [INF for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def bellman_ford(graph, start):
    distance[start] = 0

    for _ in range(1, V):
        for v in graph:
            for w, c in graph[v]:
                if distance[c] > (d := (distance[v] + w)):
                    distance[c] = d
    
    for v in graph:
        for w, c in graph[v]:
            if distance[c] > (d := (distance[v] + w)):
                return False
    
    return True


if bellman_ford(graph, 1):
    for v in range(2, V+1):
        print(distance[v] if distance[v] != INF else -1)
else:
    print(-1)