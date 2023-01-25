from math import ceil

N = int(input())

result = ""
while N:
    q = abs(N % -2)
    N = ceil(N / -2)
    result = f"{q}{result}"

print(result or 0)