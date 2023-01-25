input = __import__("sys").stdin.readline

N, K = map(int, input().split())

values = []
for _ in range(N):
    # 굳이 조건 안 걸어줘도 아래 for 문에서 걸러짐
    v = int(input())
    if v <= K:
        values.append(v)

count = 0
for i in range(len(values)-1, -1, -1):
    count += K // values[i]
    K %= values[i]

print(count)