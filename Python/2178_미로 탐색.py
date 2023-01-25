from collections import deque
input = __import__("sys").stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(N)]

# Graph construction을 명시적으로 하지는 않음
# maze를 바탕으로 "직관적인" 가상의 Graph가 있다고 가정
# Graph의 각 Node는 maze의 좌표
# 각 좌표를 Queue에 넣고 빼며 BFS 수행

deq = deque([(0, 0)])
# count = [[0] * M] * N 쓰면 안 됨 ㅋㅋ;;
# * N 때문에 동일한 ref 가진 [0, ..., 0]이 복사되는 듯
count = [[0 for _ in range(M)] for _ in range(N)]
count[0][0] = 1
visited = {(0, 0): None}

while deq:
    # 뽑음
    x, y = deq.popleft()
    # 인접한 좌표로 건너갈 수 있음?
    for a, b in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        # a, b 안 넘침? 방문한 적 없음? 미로 안 막힘?
        # 건너갈 수 있는 모든 방향으로 가면서 Queue에 밀어넣음
        if not (0 <= a < N and 0 <= b < M):
            continue
        if (a, b) in visited:
            continue
        if maze[a][b] != 1:
            continue

        # 이전까지의 값을 누적
        count[a][b] = count[x][y] + 1
        visited.setdefault((a ,b))
        deq.append((a, b))

print(count[N-1][M-1])