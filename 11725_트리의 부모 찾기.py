from sys import stdin
from collections import deque

V = int(stdin.readline())

def BFS(graph, start_V, parent_map):
    deq = deque([start_V])

    while deq:
        for v in graph[(this := deq.popleft())]:
            if v not in parent_map:
                deq.append(v)
                parent_map[v] = this
    

graph = {v:[] for v in range(1, V+1)}
for _ in range(V-1):
    v1, v2 = map(int, stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

parent_map = {}
BFS(graph, 1, parent_map)

for v in range(2, V+1):
    print(parent_map[v])