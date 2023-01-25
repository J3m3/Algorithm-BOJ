input = __import__("sys").stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split())) + [0]
# M 이하의 최대 구간합을 구해야 함
# [2, 20, 1, 2, ...]
S = start = end = maximum = 0

while end <= N:
    if maximum < S <= M:
        maximum = S
    
    if S >= M:
        S -= arr[start]
        start += 1
    
    else:
        S += arr[end]
        end += 1

print(maximum)