from sys import stdin
from collections import deque


def BFS(graph, start_V, visitied):
    deq = deque([start_V])

    while deq:
        this = deq.popleft()

        if this not in visitied:
            visitied.setdefault(this)
            deq += graph[this]


V, E = map(int, stdin.readline().split())

graph = {v: [] for v in range(1, V+1)}
for _ in range(E):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 각 정점을 시작 지점으로 해서 BFS 수행
# BFS가 수행된 횟수로 connected component 개수 판단
count = 0
cluster = {}
for vertex in range(1, V+1):
    # vertex가 cluster에 없을 경우만
    if vertex not in cluster:
        BFS(graph, vertex, cluster)
        count += 1

print(count)