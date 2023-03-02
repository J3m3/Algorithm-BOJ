from collections import deque
input = __import__("sys").stdin.readline


def check_weak(init_color, cur_color):
    if weak_map[init_color] != weak_map[cur_color]:
        return True
    return False


def check_normal(init_color, cur_color):
    if init_color != cur_color:
        return True
    return False


def bfs(x, y, checker):
    queue = deque([(y, x)])
    visited[y][x] = 1
    init_color = board[y][x]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            if visited[ny][nx]:
                continue
            
            if checker(init_color, board[ny][nx]):
                continue

            queue.append((ny, nx))
            visited[ny][nx] = 1



N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

weak_map = {"R": 0, "G": 0, "B": 1}

for cb in [check_normal, check_weak]:
    visited = [[0] * N for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(x, y, cb)
                count += 1
    print(count)