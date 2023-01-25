from collections import deque
input = __import__("sys").stdin.readline

V = int(input())
E = int(input())

graph = {v:[] for v in range(1, V+1)}
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = {}
deq = deque([1])

# 1이 포함된 connected component의 len 구하기
while deq:
    if (this := deq.popleft()) not in visited:
        visited.setdefault(this)
        deq += graph[this]

print(len(visited) - 1)