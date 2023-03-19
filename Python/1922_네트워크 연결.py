input = __import__("sys").stdin.readline

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    parent[a] = b
    return True


N = int(input())
M = int(input())

edges = [[*map(int, input().split())] for _ in range(M)]
parent = [i for i in range(N+1)]
result = 0

edges.sort(key=lambda x: x[2])

for u, v, c in edges:
    if (union(u, v)):
        result += c

print(result)
