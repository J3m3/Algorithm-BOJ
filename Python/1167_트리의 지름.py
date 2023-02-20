from collections import deque

def bfs(start):
    visited[start] = True
    queue = deque([(0, start)])
    max_cost = 0
    end_node = 0

    while queue:
        w, v = queue.popleft()
        for child_w, child_v in graph[v]:
            if not visited[child_v]:
                total = child_w + w
                if total > max_cost:
                    max_cost = total
                    end_node = child_v
                
                visited[child_v] = True
                queue.append((total, child_v))
    
    return (end_node, max_cost)


input = __import__("sys").stdin.readline

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    u, *children = map(int, input().split())
    for i in range(len(children) - 2):
        if i % 2 == 0:
            v = children[i]
            w = children[i+1]
            graph[u].append((w, v))

visited = [False] * (V+1)
end_node, max_cost = bfs(1)

visited = [False] * (V+1)
_, max_cost = bfs(end_node)

print(max_cost)