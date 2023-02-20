input = __import__("sys").stdin.readline

N, target = map(int, input().split())
arr = list(map(int, input().split()))

masks = [1 << i for i in range(N)]
count = 0
for i in range(1 << N):
    result = [ss for ss, mask in zip(arr, masks) if mask & i]
    if result and sum(result) == target:
        count += 1

print(count)

# -------------------------------------------

input = __import__("sys").stdin.readline

N, target = map(int, input().split())
arr = list(map(int, input().split()))

masks = [1 << i for i in range(N)]
count = 0
for i in range(1, 1 << N):
    total = 0
    for n in range(N):
        if masks[n] & i:
            total += arr[n]

    if total == target:
        count += 1

print(count)

# -------------------------------------------

input = __import__("sys").stdin.readline

def count_target(depth, total):
    if depth == N:
        if total == target:
            global count
            count += 1
        return
    
    count_target(depth+1, total + arr[depth])
    count_target(depth+1, total)

N, target = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
count_target(0, 0)
print(count if target else count - 1)