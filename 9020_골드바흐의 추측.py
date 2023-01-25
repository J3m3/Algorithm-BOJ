import sys

limit = 10000
sieve = [False, False] + [True] * (limit-1)

for i in range(2, int(limit**0.5)+1):
    if sieve[i]:
        for j in range(i + i, limit+1, i):
            sieve[j] = False

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    p1 = p2 = n // 2
    while True:
        if sieve[p1] and sieve[p2]:
            print(p1, p2)
            break

        p1 -= 1
        p2 += 1