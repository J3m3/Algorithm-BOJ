from collections import deque
input = __import__("sys").stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    _, *seq = list(map(int, input().split()))
    for i in range(len(seq) - 1):
        indegree[seq[i+1]] += 1
        graph[seq[i]].append(seq[i+1])

queue = deque([])
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
for _ in range(N):
    if not queue:
        print(0)
        break

    cur = queue.popleft()
    result.append(cur)

    for child in graph[cur]:
        indegree[child] -= 1
        if indegree[child] == 0:
            queue.append(child)
else:
    print(*result, sep="\n")
