import heapq
import math
input = __import__("sys").stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distances = {v: math.inf for v in range(1, V+1)}
distances[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    this_w, this_v = heapq.heappop(pq)

    if distances[this_v] < this_w:
        continue

    for child_w, child_v in graph[this_v]:
         if (distance := this_w + child_w) < distances[child_v]:
            distances[child_v] = distance
            heapq.heappush(pq, (distance, child_v))

for v in range(1, V+1):
    print(distances[v] if distances[v] != math.inf else "INF")