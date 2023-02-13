from collections import deque
input = __import__("sys").stdin.readline

MAX = 101
N, M = map(int, input().split())
visited = [0] * (MAX)
move_map = [0] * (MAX)
for _ in range(N+M):
    u, v = map(int, input().split())
    move_map[u] = v

# 6개 숫자들 돌면서 1씩 더함.
# 만약 사다리 혹은 뱀을 만나면, 그곳으로 넘어가서 "똑같은 수" 기록.
# 사다리 혹은 뱀을 만나지 않았다면, 이전 값에 1씩 더해가면서, 100 만나면 break.
# 방문 처리는 더해지는 값으로 함.
# 중요: 뱀 혹은 사다리를 만나면, 반드시 그곳으로 넘어가야 함.
#       == queue에 뱀 혹은 사다리의 시작점은 올 수 없음.

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        this = queue.popleft()
        if this == 100:
            break

        for child in range(this+1, this+7):
            if child < MAX and not visited[child]:
                # 1. 탈 사다리나 뱀이 있는지 검사.
                # 2. 있으면 무조건 넘어감.
                # 3. 넘어간 뒤, 그곳 방문한 적 있으면 큐에도 안 넣고, 로직도 수행 안 함.
                # 4. 방문한 적 없으면 큐에 넣고 로직 수행.
                # 5. 탈 사다리나 뱀이 없다면, 방문 여부만 판단하고 로직 수행.

                visited[child] = visited[this] + 1

                if move_map[child]:
                    if not visited[move_map[child]]:
                        child = move_map[child]
                        queue.append(child)
                        visited[child] = visited[this] + 1
                else:
                    queue.append(child)
                

bfs(1)
print(visited[-1] - 1)