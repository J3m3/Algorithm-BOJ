input = __import__("sys").stdin.readline

N, size = map(int, input().split())
arr = [*map(int, input().split())]

# sliding window
maximum = sum(arr[:size])
result = maximum
for i in range(size, len(arr)):
    result += arr[i] - arr[i - size]
    if result > maximum:
        maximum = result

print(maximum)