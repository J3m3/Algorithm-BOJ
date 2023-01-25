import sys

length = int(input())

original = list(map(int, sys.stdin.readline().split()))
data = {n:i for i, n in enumerate(sorted(list(set(original))))}

for num in original:
    print(data[num], end=' ')

# list.index(num)은 O(n)
# dict[num]은 O(1)