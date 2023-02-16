from collections import deque

'''
Tree 구조에서 BFS를 진행하는 경우...
1. 매번 child를 방문한 뒤 parent를 기록한다고 가정할 때,
2. 새로 방문되는 child는 "항상 parent 미기록 상태"

이를 이용해 모든 vertex에 대해 BFS를 수행하면서...
1. parent가 이미 기록된 child를 만난다면, cycle이 존재한다는 의미이므로 Tree가 아님을 확인
'''
def is_tree(graph, start):
    queue = deque([start])
    parent_map[start] = -1

    while queue:
        this = queue.popleft()
        for child in graph[this]:
            if parent_map[this] == child:
                continue
            if parent_map[child]:
                return False

            queue.append(child)
            parent_map[child] = this
        
    return True


input = __import__("sys").stdin.readline
i = 0

while True:
    i += 1
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break

    parent_map = [0] * (V+1)
    graph = {v:[] for v in range(1, V+1)}
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    tree_count = 0

    for v in range(1, V+1):
        if not parent_map[v]:
            if is_tree(graph, v):
                tree_count += 1

    if tree_count > 1:
        print(f"Case {i}: A forest of {tree_count} trees.")
    elif tree_count == 1:
        print(f"Case {i}: There is one tree.")
    else:
        print(f"Case {i}: No trees.")