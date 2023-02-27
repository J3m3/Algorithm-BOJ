from collections import deque
input = __import__("sys").stdin.readline

def move_all(frm, to, cur):
    amount = cur[frm]
    cur[frm] = 0
    cur[to] += amount
    return tuple(cur)


def move_partial(frm, to, cur):
    amount = limits[to] - cur[to]
    cur[to] = limits[to]
    cur[frm] -= amount
    return tuple(cur)


def bfs(s: tuple):
    queue = deque([s])
    while queue:
        cur = queue.popleft()

        for i, amount in enumerate(cur):
            if amount == 0:
                continue

            for j in range(3):
                if i == j:
                    continue

                if amount + cur[j] > limits[j]:
                    res = move_partial(i, j, list(cur))
                else:
                    res = move_all(i, j, list(cur))
                
                if res not in visited:
                    queue.append(res)
                    visited.add(res)
    

limits = [*map(int, input().split())]
start = (0, 0, limits[2])
visited = set()
visited.add(start)

bfs(start)
result = sorted(node[2] for node in visited if node[0] == 0)
print(*result)