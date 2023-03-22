input = __import__("sys").stdin.readline

def dfs(root):
    visited[root] = 1
    for child in tree[root]:
        if not visited[child]:
            if root in skips:
                skips.add(child)
            if child == target:
                deletes.append(root)
            dfs(child)

# Inputs
N = int(input())
nodes = [*map(int, input().split())]
target = int(input())

# preparation for dfs
visited = [0] * N
root = None

deletes = [] # denotes children that will be removed
skips = set([target]) # denotes parents that will be removed

tree = [set() for _ in range(N)]
for child, parent in enumerate(nodes):
    if parent == -1:
        root = child
        continue
    tree[parent].add(child)

dfs(root)

for d in deletes:
    tree[d].discard(target)

count = 0
for parent, children in enumerate(tree):
    if parent not in skips and not children:
        count += 1
print(count)
