from collections import deque
input = __import__("sys").stdin.readline


def check_board(visited):
    count = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0 and board[y][x] == 0:
                count += 1
    return count


def bfs():
    visited = [[0] * M for _ in range(N)]
    queue = deque(starts)
    for coord in starts:
        visited[coord[0]][coord[1]] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= nx < M and 0 <= ny < N):
                continue

            if visited[ny][nx]:
                continue

            if board[ny][nx] == 1:
                continue

            queue.append((ny, nx))
            visited[ny][nx] = 1
    
    return check_board(visited)


def dfs(s: int, l: list):
    if len(l) == 3:
        for coord in l:
            y, x = coord
            board[y][x] = 1
        count = bfs()
        for coord in l:
            y, x = coord
            board[y][x] = 0
    
        global max_count
        if max_count < count:
            max_count = count

        return

    for i in range(s, len(more_blocks)):
        l.append(more_blocks[i])
        dfs(i+1, l)
        l.pop()


N, M = map(int, input().split())
starts = []
more_blocks = []
board = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for y in range(N):
    line = list(map(int, input().split()))
    board.append([*line])
    for x in range(M):
        if line[x] == 2:
            starts.append((y, x))
        elif line[x] == 0:
            more_blocks.append((y, x))

max_count = 0
dfs(0, [])
print(max_count)