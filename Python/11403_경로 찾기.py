input = __import__("sys").stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                continue

            if board[i][k] and board[k][j]:
                board[i][j] = 1

for line in board:
    print(*line)
