from collections import deque
from sys import stdin
input = stdin.readline
MAX = 100001

N, K = map(int, input().split())
visited = {}

def bfs(start):
    dq = deque([start])
    visited[start] = 0

    while dq:
        v = dq.popleft()
        if v == K:
            print(visited[v])
            break

        for val in [v * 2, v + 1, v - 1]:
            # The maximum length of visited could be 100000
            # so there might be hash collision in visited dictionary
            # Instead, we can use array[100001] to guarantee the accessing time complexity of O(1)
            if 0 <= val < MAX and not visited.get(val):
                if val == v * 2:
                    visited[val] = visited[v]
                    dq.appendleft(val)
                else:
                    visited[val] = visited[v] + 1
                    dq.append(val)

bfs(N)

# -------------------------------

from collections import deque
from sys import stdin
input = stdin.readline
MAX = 100001

N, K = map(int, input().split())
visited = [-1 for _ in range(MAX)] # use array instead of dictionary

def bfs(start):
    dq = deque([start])
    visited[start] = 0

    while dq:
        v = dq.popleft()
        if v == K:
            print(visited[v])
            break

        for val in [v * 2, v + 1, v - 1]:
            if 0 <= val < MAX and visited[val] == -1:
                if val == v * 2:
                    visited[val] = visited[v]
                    dq.appendleft(val)
                else:
                    visited[val] = visited[v] + 1
                    dq.append(val)

bfs(N)