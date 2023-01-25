from math import ceil
import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().split())
    
    floor = n % h
    if floor == 0:
        floor += h

    room = ceil(n / h)

    print(f'{floor}{room:>02}')