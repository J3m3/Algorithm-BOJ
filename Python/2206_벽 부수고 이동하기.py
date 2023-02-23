from collections import deque
input = __import__("sys").stdin.readline

N, M = map(int, input().split())
board = [[[0] * M for _ in range(N)] for _ in range(2)]

for i in range(N):
    for j, coord in enumerate(map(int, input().rstrip())):
        board[0][i][j] = coord
        board[1][i][j] = coord

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

board[0][0][0] = -1
board[1][0][0] = -1

queue = deque([(0, 0, 0)])
while queue:
    w, y, x = queue.popleft()
    if x == M - 1 and y == N - 1:
        print(abs(board[w][y][x]))
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < M and 0 <= ny < N):
            continue

        if w:
            if board[w][ny][nx] != 0:
                continue
            
            board[w][ny][nx] = board[w][y][x] - 1
            queue.append((w, ny, nx))

        else:
            if board[w][ny][nx] < 0:
                continue

            if board[w][ny][nx] == 1:
                w = 1

            board[w][ny][nx] = board[0][y][x] - 1
            queue.append((w, ny, nx))
            w = 0
else:
    print(-1)

# -----------------------------------------------------

from collections import deque
input = __import__("sys").stdin.readline

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        used_wall, y, x = queue.popleft()
        if x == M - 1 and y == N - 1:
            return visited[used_wall][y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nx < M and 0 <= ny < N):
                continue

            # 정확히 한 번만 벽을 부수고 이동할 수 있기 때문에, 방문 여부 신경 쓰지 않아도 됨
            if board[ny][nx] == WALL and not used_wall:
                visited[WALL][ny][nx] = visited[PATH][y][x] + 1
                queue.append((WALL, ny, nx))
                
            elif board[ny][nx] == PATH and not visited[used_wall][ny][nx]:
                visited[used_wall][ny][nx] = visited[used_wall][y][x] + 1
                queue.append((used_wall, ny, nx))
    
    return -1


PATH = 0
WALL = 1
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

print(bfs())