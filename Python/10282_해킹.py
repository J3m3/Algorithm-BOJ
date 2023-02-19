from heapq import heappop, heappush
input = __import__("sys").stdin.readline
INF = float('inf')


def dijkstra(start):
    distance[start] = 0
    start = (0, start)
    pq = [start]

    while pq:
        w, v = heappop(pq)

        if distance[v] < w:
            continue

        for c_w, c_v in graph[v]:
            if distance[c_v] > (d := (c_w + w)):
                distance[c_v] = d
                heappush(pq, (d, c_v))


T = int(input())
for _ in range(T):
    V, E, hacked = map(int, input().split())

    graph = {v:[] for v in range(1, V+1)}
    distance = [INF for _ in range(V+1)]

    for _ in range(E):
        u, v, s = map(int, input().split())
        graph[v].append((s, u))
    
    dijkstra(hacked)

    count = 0
    time = 0
    for cost in distance:
        if cost != INF:
            count += 1
            time = max(time, cost)
    
    print(count, time)
