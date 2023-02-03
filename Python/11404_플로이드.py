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