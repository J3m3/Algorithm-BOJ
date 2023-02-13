input = __import__("sys").stdin.readline

N = int(input())
a, b = 1, 2
for i in range(N-1):
    b, a = (a + b) % 10007, b % 10007

print(a)
