input = __import__("sys").stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    max_count = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_count = max(max_count, dp[j])
    
    dp[i] += max_count

length = max(dp)
print(length)

result = []
for i in range(N-1, -1, -1):
    if dp[i] == length:
        result.append(arr[i])
        length -= 1

print(*reversed(result))