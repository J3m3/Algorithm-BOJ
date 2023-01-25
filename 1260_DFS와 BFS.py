from sys import stdin
from collections import deque
from copy import deepcopy
import heapq

def DFS(adj_list, start_V):
    stack = [start_V]
    visited = {}

    while stack:
        this = stack.pop()

        if this not in visited:
            visited.setdefault(this)

            tmp = deque([])
            while adj_list[this]:
                child = heapq.heappop(adj_list[this])
                tmp.appendleft(child)
            stack += tmp
    
    return visited


def BFS(adj_list, start_V):
    deq = deque([start_V])
    visited = {}
    
    while deq:
        this = deq.popleft()
        if this not in visited:
            visited.setdefault(this)

            while adj_list[this]:
                child = heapq.heappop(adj_list[this])
                deq.append(child)
    
    return visited


V, E, start_V = map(int, stdin.readline().split())
adj_list = {v:[] for v in range(1, V+1)}

for _ in range(E):
    v1, v2 = map(int, stdin.readline().split())
    heapq.heappush(adj_list[v1], v2)
    heapq.heappush(adj_list[v2], v1)

print(*DFS(deepcopy(adj_list), start_V))
print(*BFS(adj_list, start_V))