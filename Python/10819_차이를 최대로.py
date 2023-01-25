input = __import__("sys").stdin.readline

N = int(input())
input_arr = list(map(int, input().split()))
visited = [False] * N
Max = 0
def DFS(level, arr: list):
    if level == N:
        total = 0
        for i in range(N-1):
            total += abs(arr[i] - arr[i+1])
        
        global Max
        if Max < total:
            Max = total

        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(input_arr[i])

            DFS(level+1, arr)

            visited[i] = False
            arr.pop()

DFS(0, [])
print(Max)