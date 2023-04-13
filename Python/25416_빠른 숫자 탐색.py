from collections import deque
input = __import__("sys").stdin.readline

def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = 1

    while queue:
        y, x = queue.popleft()
        if board[y][x] == 1:
            return visited[y][x] - 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            
            if visited[ny][nx]:
                continue

            if board[ny][nx] == -1:
                continue

            queue.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1
    
    return -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [[*map(int, input().split())] for _ in range (5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
r, c = map(int, input().split())
print(bfs(r, c))
