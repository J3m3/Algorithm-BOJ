import heapq

def distances_init(distances):
    for key in distances:
        distances[key] = INF

def dijkstra(start):
    pq = []
    distances[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        this_w, this_v = heapq.heappop(pq)

        if distances[this_v] < this_w:
            continue

        for child_w, child_v in graph[this_v]:
            if distances[child_v] > (distance := this_w + child_w):
                distances[child_v] = distance
                heapq.heappush(pq, (distance, child_v))


input = __import__("sys").stdin.readline
INF = float('inf')

V = int(input())
E = int(input())

graph = {}
distances = {}
for v in range(1, V+1):
    graph[v] = []
    distances[v] = INF

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

for v in range(1, V+1):
    dijkstra(v)
    for i in range(1, V+1):
        print(distances[i] if distances[i] != INF else 0, end=' ')
    print()
    distances_init(distances)

# -------------------------------------------

input = __import__("sys").stdin.readline
INF = float('inf')

V = int(input())
E = int(input())

graph = [[INF if i != j else 0 for i in range(V)] for j in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = min(graph[u-1][v-1], w)

for m in range(V):
    for u in range(V):
        for v in range(V):
            graph[u][v] = min(graph[u][v], graph[u][m] + graph[m][v])

for i in range(V):
    for j in range(V):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()