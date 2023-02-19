from heapq import heappop, heappush
input = __import__("sys").stdin.readline
INF = float('inf')


def dijkstra(start):
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        this_w, this_v = heappop(pq)

        if distance[this_v] < this_w:
            continue

        for child_w, child_v in graph[this_v]:
            if distance[child_v] > (d := (child_w + this_w)):
                distance[child_v] = d
                heappush(pq, (d, child_v))


V, E, X = map(int, input().split())
graph = {v:[] for v in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance_boards = [[]]
for v in range(1, V+1):
    distance = [INF for _ in range(V+1)]
    dijkstra(v)
    distance_boards.append(distance)

max_consumption = 0
for v in range(1, V+1):
    max_consumption = max(max_consumption, distance_boards[v][X] + distance_boards[X][v])

print(max_consumption)

# ------------------------------------------

from heapq import heappop, heappush
input = __import__("sys").stdin.readline
INF = float("inf")

def dijkstra(graph, start, distance):
    distance[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        this_w, this_v = heappop(pq)

        if distance[this_v] < this_w:
            continue

        for child_w, child_v in graph[this_v]:
            if (distance[child_v] > (d := (this_w + child_w))):
                distance[child_v] = d
                heappush(pq, (d, child_v))


V, E, X = map(int, input().split())

graph_dep = {}
graph_dest = {}
distance_dep = [INF]
distance_dest = [INF]
for v in range(1, V+1):
    graph_dep[v] = []
    graph_dest[v] = []
    distance_dep.append(INF)
    distance_dest.append(INF)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph_dep[u].append((w, v))
    graph_dest[v].append((w, u))

dijkstra(graph_dep, X, distance_dep)
dijkstra(graph_dest, X, distance_dest)

max_consumption = 0
for i in range(1, V+1):
    max_consumption = max(max_consumption, distance_dep[i] + distance_dest[i])

print(max_consumption)