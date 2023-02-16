# TLE with Floyd-Warshall in Python 3

from heapq import heappush, heappop
input = __import__("sys").stdin.readline
MAX = float('inf')

'''
1. 모든 edge(정확히는 jump 횟수가 1인 path)를 PQ에 push
2. 최소 가중치 path부터 pop해가면서,
3. path의 jump 길이를 cycle이 만들어질 때까지 늘림
4. 최소 가중치 path부터 처리하고 있으므로, 최단 거리 cycle == 최초로 만들어지는 cycle
   (dijkstra의 greedy함과 연관... "한 번 pop됐으면, 현재까지는 그것이 최소 거리")
'''

V, E = map(int, input().split())
graph = {v:[] for v in range(1, V+1)}
pq = []
distances = [[MAX] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    heappush(pq, (w, u, v))

while pq:
    w, frm, to = heappop(pq)

    if frm == to:
        print(w)
        break

    if distances[frm][to] < w:
        continue

    for end_w, end in graph[to]:
        if distances[frm][end] > (d := (w + end_w)):
            distances[frm][end] = d
            heappush(pq, (d, frm, end))
else:
    print(-1)