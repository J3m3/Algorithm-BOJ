input = __import__("sys").stdin.readline

factorials = [1] * 31
for i in range(2, 31):
    factorials[i] = factorials[i-1] * i

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(factorials[M] // (factorials[N] * factorials[M-N]))
