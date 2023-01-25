input = __import__("sys").stdin.readline

size, N = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
cumulated = [0] + [total := (total + num) for num in arr]

# arr: [5,4,3,2,1]
# cumulated: [0, 5, 9, 12, 14, 15]
# 구간합: arr[e] - arr[s-1]

for _ in range(N):
    s, e = map(int, input().split())
    print(cumulated[e] - cumulated[s-1])