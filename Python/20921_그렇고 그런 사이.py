input = __import__("sys").stdin.readline

def count_some(arr, target):
    if target == 0:
        return arr
    
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
            if count == K:
                return arr

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
print(*count_some(arr, K))