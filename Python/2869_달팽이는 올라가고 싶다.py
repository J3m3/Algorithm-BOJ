from math import ceil
a, b, v = map(int, input().split())
print(ceil((v - a) / (a - b)) + 1)