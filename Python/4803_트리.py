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

# ---------------------------------------

input = __import__("sys").stdin.readline

def find(parent, u):
    if parent[u] == u:
        return u
    parent[u] = find(parent, parent[u])
    return parent[u]    

def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)

    if u > v:
        parent[u] = v
    else:
        parent[v] = u

def is_union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)
    return True if u == v else False

case = 0
while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break

    case += 1

    # 입력된 두 vertex를 매번 통일된 기준(이 경우, u > v)으로 union
    # 만약 cycle이 발견된 경우(= 두 vertex가 같은 cluster 내 존재), 둘 중 아무 vertex를 기록
    cycles = []
    parent = [i for i in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        if is_union(parent, u, v):
            cycles.append(u)
        else:
            union(parent, u, v)

    # 같은 cluster에 속한 vertex는 모두 통일된 하나의 parent를 바라보도록 함
    for i in range(1, V+1):
        find(parent, i)
    
    # 기록해 둔 cycles 리스트의 vertex들을 하나씩 확인하며,
    # 해당 vertex가 속하는 cluster의 대푯값인 parent[v]를 기록
    # 즉, cycle이 발생한 cluster를 parent[v]를 identifier로 하여 판단 가능
    cycle_roots_group = set()
    for v in cycles:
        cycle_roots_group.add(parent[v])
    
    # 해당 cluster가 cycle이 있는 cluster라면 Tree가 아니므로 건너뛰고,
    # cycle이 없는 cluster라면 result++ 한 뒤,
    # 그 cluster는 이미 확인했다는 의미에서 검증용 set에 추가 (중복 방지)
    result = 0
    for i in range(1, V+1):
        if parent[i] in cycle_roots_group:
            continue
        cycle_roots_group.add(parent[i])
        result += 1
    
    if result == 0:
        print(f"Case {case}: No trees.")
    elif result == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {result} trees.")