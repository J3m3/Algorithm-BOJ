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

# ------------------------------------

input = __import__("sys").stdin.readline

N = int(input())
count = 0
col_visited = [False] * (2*N+1)
sum_rowcol_map = [False] * (2*N+1)
sub_rowcol_map = [False] * (2*N+1)

def DFS(r):
    if r == N:
        global count
        count += 1
        return
    
    for c in range(N):
        if col_visited[c] or sum_rowcol_map[r+c] or sub_rowcol_map[r-c+N-1]:
            continue

        col_visited[c] = True
        sum_rowcol_map[r+c] = True
        sub_rowcol_map[r-c+N-1] = True

        DFS(r+1)

        col_visited[c] = False
        sum_rowcol_map[r+c] = False
        sub_rowcol_map[r-c+N-1] = False

DFS(0)
print(count)