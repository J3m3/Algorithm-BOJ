from collections import deque
input = __import__("sys").stdin.readline

N, start, end, U, D = map(int, input().split())
visited = [0] * 1000002
queue = deque([start])
visited[start] = 1

while queue:
    cur = queue.popleft()
    if cur == end:
        print(visited[end] - 1)
        break
    
    for nxt in [cur + U, cur - D]:
        if 0 < nxt <= N and not visited[nxt]:
            queue.append(nxt)
            visited[nxt] = visited[cur] + 1
else:
    print("use the stairs")
