from collections import deque
input = __import__("sys").stdin.readline

MAX = int(input()) + 1
input()

queue = deque(map(int, input().split()))
MAX_ITER = len(bin(MAX - 1)) - 2
visited = [-1] * MAX

def bfs():
    max_sscore = 0

    for i in queue:
        visited[i] = 0

    while queue:
        this = queue.popleft()

        for i in range(MAX_ITER):
            child = this ^ (1 << i)

            if child < MAX and visited[child] == -1:
                visited[child] = visited[this] + 1
                queue.append(child)
                max_sscore = max(max_sscore, visited[child])
    
    print(max_sscore)

bfs()