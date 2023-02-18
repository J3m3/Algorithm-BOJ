input = __import__("sys").stdin.readline

def find(parent, n):
    if parent[n] == n:
        return n
    
    parent[n] = find(parent, parent[n])
    return parent[n]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if rank[a] > rank[b]:
        parent[b] = a
        rank[a] += 1
    else:
        parent[a] = b
        rank[b] += 1


N = int(input()) # <= 200
M = int(input()) # <= 1000

parent = [i for i in range(N+1)]
rank = [1 for _ in range(N+1)]

for i in range(N):
    t = list(map(int, input().split()))
    for j in range(i+1, N):
        if t[j]:
            union(parent, i+1, j+1)

schedule = list(map(int, input().split()))
p = find(parent, schedule[0])
for v in schedule:
    if p != find(parent, v):
        print("NO")
        break
else:
    print("YES")