input = __import__("sys").stdin.readline

length = int(input())
num_list = list(map(int, input().split()))
maximum = max(num_list)
seive = [False, False] + [True] * (maximum-1)

for i in range(2, int(maximum ** 0.5)+1):
    if seive[i]:
        for j in range(i+i, maximum+1, i):
            seive[j] = False

total = 1
for n in num_list:
    if seive[n]:
        seive[n] = False
        total *= n

print(total if total > 1 else -1)