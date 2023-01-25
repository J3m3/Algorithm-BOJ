import sys

n = start = int(sys.stdin.readline().rstrip())
cycle = 0

while True:
    n = n % 10 * 10 + (n // 10 + n % 10) % 10
    cycle += 1

    if n == start:
        break

print(cycle)