input = __import__("sys").stdin.readline

N = int(input())
visited = [False] * (N+1)

def dfs(arr):
    if len(arr) == N:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(arr)
            arr.pop()
            visited[i] = False

dfs([])