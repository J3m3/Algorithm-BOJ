import sys

limit = 123456 * 2
sieve = [False, False] + [True] * (limit-1)

for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i + i, limit + 1, i):
            sieve[j] = False

for n in map(int, sys.stdin.read().split()):
    if n == 0:
        break

    print(sum(sieve[n + 1:2 * n + 1]))