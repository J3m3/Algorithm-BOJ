input = __import__("sys").stdin.readline

N = int(input())

a, b = 1, 3
if N & 1:
    print(0)
else:
    for i in range(0, N, 2):
        b, a = 4 * b - a, b
    print(a)
