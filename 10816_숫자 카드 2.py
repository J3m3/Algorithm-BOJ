input = __import__("sys").stdin.readline

input()
d = {}
for n in map(int, input().split()):
    d[n] = d.get(n, 0) + 1
input()
for num in map(int, input().split()):
    print(d.get(num, 0))

# ------------------------

input = __import__("sys").stdin.readline

def find_upper_bound(arr, num, l, r):
    if l >= r:
        return r

    mid = (l + r) // 2

    if num < arr[mid]:
        return find_upper_bound(arr, num, l, mid)
    
    else:
        return find_upper_bound(arr, num, mid+1, r)


def find_lower_bound(arr, num, l, r):
    if l >= r:
        return r

    mid = (l + r) // 2

    if num <= arr[mid]:
        return find_lower_bound(arr, num, l, mid)
    
    else:
        return find_lower_bound(arr, num, mid+1, r)

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())

for num in map(int, input().split()):
    lb = find_lower_bound(arr, num, 0, N)
    rb = find_upper_bound(arr, num, 0, N)

    print(rb - lb, end=" ")