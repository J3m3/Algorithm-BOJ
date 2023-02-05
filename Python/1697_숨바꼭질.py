from collections import deque
input = __import__("sys").stdin.readline

MAX = 100001
visited = {}

N, K = map(int, input().split())

def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        this = queue.popleft()

        if this == K:
            print(visited[this])
            return

        for val in [this-1, this+1, this << 1]:
            if 0 <= val < MAX and not visited.get(val):
                visited[val] = visited[this] + 1
                queue.append(val)

bfs(N)