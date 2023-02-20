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