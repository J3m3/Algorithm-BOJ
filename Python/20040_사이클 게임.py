import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find(parent, a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return True

    if rank[a] > rank[b]:
        parent[b] = a
        rank[a] += 1
    else:
        parent[a] = b
        rank[b] += 1
    
    return False


N, M = map(int, input().split())
rank = [1 for _ in range(N)]
parent = [i for i in range(N)]

result = []
for i in range(1, M+1):
    a, b = map(int, input().split())
    if union(parent, a, b):
        result.append(i)

if result:
    print(result[0])
else:
    print(0)