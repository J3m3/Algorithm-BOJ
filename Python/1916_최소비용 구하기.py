from heapq import heappop, heappush
input = __import__("sys").stdin.readline
INF = float('inf')

def dijkstra(s):
    pq = [(0, s)]
    distance[s] = 0

    while pq:
        cur_w, cur_v = heappop(pq)

        if distance[cur_v] < cur_w:
            continue

        for child_w, child_v in graph[cur_v]:
            if (d := child_w + cur_w) < distance[child_v]:
                distance[child_v] = d
                heappush(pq, (d, child_v))

N = int(input())
M = int(input())

graph = {}
distance = {}
for v in range(1, N+1):
    graph[v] = []
    distance[v] = INF

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((c, v))

S, E = map(int, input().split())
dijkstra(S)
print(distance[E])