input = __import__("sys").stdin.readline

N = int(input())

total = 0
dp_sum = 0
for time in sorted(map(int, input().split())):
    total += (dp_sum := (dp_sum + time))

print(total)