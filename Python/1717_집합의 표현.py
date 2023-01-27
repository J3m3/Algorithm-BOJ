input = __import__("sys").stdin.readline

# 0: union
# 1: find
n, m = map(int, input().split())
parent = [0] + [i for i in range(1, n+1)]
height = [1] * (n+1)

def union(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return

    if height[u] < height[v]:
        parent[u] = v
    else:
        parent[v] = u
        if height[u] == height[v]:
            height[u] += 1

def find(u):
    if u == parent[u]:
        return u
    
    v = find(parent[u])
    parent[u] = v
    return v

def is_union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        print("YES")
        return
    print("NO")

cmd_map = {
    0: union,
    1: is_union
}

for _ in range(m):
    cmds = [*map(int, input().split())]
    cmd_map[cmds[0]](cmds[1], cmds[2])