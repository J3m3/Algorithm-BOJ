from collections import deque
input = __import__("sys").stdin.readline

N = int(input())
graph = {v:[] for v in range(1, N+1)}
visited = [-1] * (N+1)

for i in range(1, N+1):
    for j in map(int, input().split()):
        if j != 0:
            graph[i].append(j)

input()
starts = map(int, input().split())

# 이웃한 정점들 돌아야 함.
# 이때 visited 배열의 업데이트를 pop할 때로 미뤄야 함.
# 즉, 어떤 정점의 child들을 도는 행위는 "동시에" 일어남.
# "동시에"를 구현하기 위해 이전 노드가 다음 노드에 루머 전달할 때마다 infected_checker[다음노드] -= 1
# 이러면 가장 마지막에 루머 전달하는 노드 == 주변 절반 이상 감염됐을 때 최초로 루머 전달하는 노드
def bfs():
    queue = deque(starts)
    for v in queue:
        visited[v] = 0
    
    infected_checker = [0] + [(len(graph[i]) + 1) // 2 for i in range(1, N+1)]

    while queue:
        this = queue.popleft()
        for child in graph[this]:
            if visited[child] == -1:
                infected_checker[child] -= 1
                if infected_checker[child] <= 0:
                    queue.append(child)
                    visited[child] = visited[this] + 1


bfs()
print(*visited[1:])