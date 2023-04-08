input = __import__("sys").stdin.readline

N, C = map(int, input().split())
f = {}
for i in map(int, input().split()):
    f[i] = f.get(i, 0) + 1

for n, freq in sorted(list(f.items()), key=lambda x: -x[1]):
    for _ in range(freq):
        print(n, end=" ")
