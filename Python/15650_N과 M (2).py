input = __import__("sys").stdin.readline

n, r = map(int, input().split())

def dfs(arr, start):
    if len(arr) == r:
        print(*arr)
        return

    for i in range(start, n+1):
        arr.append(i)
        dfs(arr, i+1)
        arr.pop()

dfs([], 1)