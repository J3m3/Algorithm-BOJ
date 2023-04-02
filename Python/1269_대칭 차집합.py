input = __import__("sys").stdin.readline

input()

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A ^ B))
