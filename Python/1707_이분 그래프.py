from collections import deque
input = __import__("sys").stdin.readline

def bfs(graph, start):
    visited[start] = 0
    queue = deque([start])

    while queue:
        this = queue.popleft()
        for child in graph[this]:
            if visited[this] == visited[child]:
                return False

            if visited[child] == -1:
                queue.append(child)
                visited[child] = (visited[this] + 1) % 2
    
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = {}
    visited = {}
    for v in range(1, V+1):
        graph[v] = []
        visited[v] = -1

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V+1):
        if visited[i] == -1:
            if not bfs(graph, i):
                print("NO")
                break
    else:
        print("YES")