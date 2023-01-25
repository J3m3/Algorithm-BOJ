input = __import__("sys").stdin.readline
n, r = map(int, input().split())
visited = [False] * (n+1)

def dfs(arr):
    if len(arr) == r:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(arr)
            arr.pop()
            visited[i] = False

dfs([])