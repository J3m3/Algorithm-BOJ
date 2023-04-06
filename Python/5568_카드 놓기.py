from itertools import permutations
input = __import__("sys").stdin.readline

n = int(input())
k = int(input())

cards = [int(input()) for _ in range(n)]

result = set()
for p in permutations(cards, k):
    result.add("".join(map(str, p)))

print(len(result))
