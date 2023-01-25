input = __import__("sys").stdin.readline

N, M = map(int, input().split())

l = sorted(input().rstrip() for _ in range(N+M))

count = 0
result = []
for i in range(len(l)-1):
    if l[i] == l[i+1]:
        count += 1
        result.append(l[i])

print(count)
print(*result, sep='\n')