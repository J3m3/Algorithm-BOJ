# TLE with Python
input = __import__("sys").stdin.readline

N = int(input())
visited = [False] * N

def is_diag(arr, new_q):
    for i, q in enumerate(arr):
        if len(arr) - i == abs(new_q - q):
            return False
    return True

def dfs(arr):
    if len(arr) == N:
        global count
        count += 1
        return
    
    for i in range(N):
        if not visited[i] and is_diag(arr, i):
            arr.append(i)
            visited[i] = True
            dfs(arr)
            arr.pop()
            visited[i] = False

count = 0
dfs([])
print(count)