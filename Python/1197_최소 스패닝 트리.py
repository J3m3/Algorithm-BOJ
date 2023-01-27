input = __import__("sys").stdin.readline

def union(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return
    
    if u < v:
        roots[u] = v
    else:
        roots[v] = u

def find(u):
    if u == roots[u]:
        return u
    roots[u] = find(roots[u])
    return roots[u]


V, E = map(int, input().split())
roots = [v for v in range(V+1)]
edge_list = []
for _ in range(E):
    edge_list.append([*map(int, input().split())])

edge_list.sort(key=lambda x: x[2])

weight_sum = 0
for u, v, w in edge_list:
    u = find(u)
    v = find(v)

    if u != v:
        union(u, v)
        weight_sum += w

print(weight_sum)