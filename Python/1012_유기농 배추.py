from collections import deque
input = __import__("sys").stdin.readline

def BFS(graph: list[list], start: tuple[int]):
    graph[start[1]][start[0]] = 0
    queue = deque([start])

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < width and 0 <= ny < height):
                continue

            if graph[ny][nx] == 0:
                continue

            graph[ny][nx] = 0
            queue.append((nx, ny))


T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    width, height, k = map(int, input().split())
    field = [[0 for _ in range(width)] for _ in range(height)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0
    for y in range(height):
        for x in range(width):
            if field[y][x] != 0:
                BFS(field, (x, y))
                count += 1

    print(count)