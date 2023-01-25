import sys

input()
for coordinate in sorted([list(map(int, x_y.split())) for x_y in sys.stdin.read().rstrip().split('\n')], key=lambda x: (x[1], x[0])):
    print(*coordinate)