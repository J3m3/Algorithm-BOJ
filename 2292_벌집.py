N = int(input())

n = 1
count = 1
while N > n:
    n += 6 * count # 계차수열
    count += 1

print(count)