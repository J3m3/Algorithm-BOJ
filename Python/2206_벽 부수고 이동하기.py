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