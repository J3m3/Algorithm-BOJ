input = __import__("sys").stdin.readline

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
count = 0

for _ in range(N):
    a, b = map(int, input().split())

    for y in range(b, b+10):
        for x in range(a, a+10):
            if paper[y][x] == 0:
                count += 1
                paper[y][x] = 1

print(count)