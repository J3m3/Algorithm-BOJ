import heapq
input = __import__("sys").stdin.readline
INF = float('inf')

def dijkstra(start):
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        this_w, this = heapq.heappop(pq)

        if distances[this] < this_w:
            continue

        for child_w, child in graph[this]:
            if distances[child] > (distance := this_w + child_w):
                distances[child] = distance
                heapq.heappush(pq, (distance, child))


def initialize_dict(dict):
    for key in dict:
        dict[key] = INF

V, E = map(int, input().split())
distances = {}
graph = {}
for v in range(1, V+1):
    graph[v] = []
    distances[v] = INF

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

v1, v2 = map(int, input().split())

# 첫 번째 다익스트라 후 v1, v2까지의 거리 구함
# v1 시작점으로 다익스트라 후 v2까지 거리 구함 (v1_to_v2 == v2_to_v1)
# v2 시작점으로 다익스트라 후 도착점까지 거리 구함
"""
min(
    d(start, v1) + d(v1, end),
    d(start, v2) + d(v2, end)
)
"""
dijkstra(1)
start_to_v1 = distances[v1]
start_to_v2 = distances[v2]
initialize_dict(distances)

dijkstra(v1)
v1_to_v2 = distances[v2]
v1_to_end = distances[V]
initialize_dict(distances)

if v1_to_v2 == INF or v1_to_end == INF:
    print(-1)

else:
    dijkstra(v2)
    v2_to_end = distances[V]

    print(
        min(
            start_to_v1 + v1_to_v2 + v2_to_end,
            start_to_v2 + v1_to_v2 + v1_to_end
        )
    )