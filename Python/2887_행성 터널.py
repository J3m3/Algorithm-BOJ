input = __import__("sys").stdin.readline

def find(a):
    if a == parent[a]:
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
xs = []
ys = []
zs = []
parent = []

for i in range(N):
    x, y, z = map(int, input().split())
    xs.append((i, x))
    ys.append((i, y))
    zs.append((i, z))
    parent.append(i)

compare = lambda x: x[1]
xs.sort(key=compare)
ys.sort(key=compare)
zs.sort(key=compare)

edges = []
for i in range(N-1):
    for coords in [xs, ys, zs]:
        u, v = coords[i][0], coords[i+1][0]
        w = abs(coords[i][1] - coords[i+1][1])
        edges.append((u, w, v))

edges.sort(key=compare)

result = 0
for u, w, v in edges:
    if union(u, v):
        result += w

print(result)
