input = __import__("sys").stdin.readline

n, r = map(int, input().split())

def dfs(arr):
    if len(arr) == r:
        print(*arr)
        return 

    for i in range(1, n+1):
        arr.append(i)
        dfs(arr)
        arr.pop()

dfs([])