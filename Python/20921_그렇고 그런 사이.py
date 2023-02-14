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

# -----------------------------------------

input = __import__("sys").stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
head = []

n = N - 1
while K:
    if K >= n:
        K -= n
        head.append(n + 1)
        arr[n] = 0
    
    n -= 1

for n in head:
    print(n, end=" ")
for n in arr:
    if n:
        print(n, end=" ")