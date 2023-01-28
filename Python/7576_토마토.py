from collections import deque
input = __import__("sys").stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(board, arr):
    queue = deque([*arr])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if board[ny][nx] != 0:
                continue
            
            queue.append((nx, ny))
            board[ny][nx] = board[y][x] + 1

starts = []
zero_count = 0
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            starts.append((x, y))
        elif board[y][x] == 0:
            zero_count += 1

if zero_count == 0:
    print(0)
else:
    bfs(board, starts)
    maximum = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                print(-1)
                break
            elif maximum < board[y][x]:
                maximum = board[y][x]
        else:
            continue
        break
    else:
        print(maximum - 1)