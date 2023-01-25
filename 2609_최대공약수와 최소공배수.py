input = __import__("sys").stdin.readline

a, b = map(int, input().split())
mul = a * b
while b > 0:
    a, b = b, a % b

print(a)
print(mul // a)