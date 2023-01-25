from collections import deque
input = __import__("sys").stdin.readline

def BFS(board, start):
    nodes = 0
    deq = deque([start])
    visited.setdefault(start)

    while deq:
        this = deq.popleft()
        for i in range(4):
            nx = this[1] + dx[i]
            ny = this[0] + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if (ny, nx) in visited:
                continue
            if board[ny][nx] == 0:
                continue
            
            visited.setdefault((ny, nx))
            deq.append((ny, nx))
        
        nodes += 1
    
    return nodes

N = int(input())
board = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 0
num_of_nodes = []

# 공간 복잡도를 줄이기 위해서 board 자체를 visited로 활용할 수도 있음
# 한번 BFS가 시작되면 방문되는 좌표의 값들을 모두 0으로 바꿔버리는 것
# 그러면 하단의 if 문의 "(y, x) not in visited" 조건도 필요하지 않음
visited = {}

for y in range(N):
    for x in range(N):
        if (y, x) not in visited and board[y][x] != 0:
            num_of_nodes.append(BFS(board, (y, x)))
            count += 1
        
print(count)
print(*sorted(num_of_nodes), sep="\n")