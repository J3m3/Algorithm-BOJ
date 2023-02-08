from collections import deque


def check_board(board):
    max_days = 0
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if board[h][y][x] == 0:
                    return -1
                
                max_days = max(max_days, board[h][y][x])
    
    return max_days - 1


def get_init_tomatoes(board):
    tomatoes = []
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if board[h][y][x] == 1:
                    tomatoes.append((x, y, h))

    return tomatoes


def bfs(board, starts):
    queue = deque([start for start in starts])

    while queue:
        x, y, h = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nh = h + dh[i]

            if not (0 <= nx < M and 0 <= ny < N and 0 <= nh < H):
                continue

            if board[nh][ny][nx] != 0:
                continue
            
            board[nh][ny][nx] = board[h][y][x] + 1
            queue.append((nx, ny, nh))


input = __import__("sys").stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomatoes = get_init_tomatoes(board)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

bfs(board, tomatoes)
print(check_board(board))