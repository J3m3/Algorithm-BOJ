from collections import deque
input = __import__("sys").stdin.readline
INF = float("inf")
MAX = 100001

def is_valid(coord):
    if 0 <= coord < MAX:
        return True
    return False

N, K = map(int, input().split())

visited = [False] * MAX
queue = deque([(N, 0)])

count = 0
min_steps = INF
while queue:
    cur, steps = queue.popleft()
    visited[cur] = True

    if count == 0 and cur == K:
        min_steps = steps

    if cur == K and steps == min_steps:
        count += 1

    if steps >= min_steps:
        continue
    
    for child in [cur - 1, cur + 1, cur << 1]:
        if is_valid(child) and not visited[child]:
            queue.append((child, steps + 1))

print(min_steps)
print(count)
