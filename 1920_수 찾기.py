input = __import__("sys").stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))
input()

def binary_search(arr, num_to_find, left, right):
    if left > right:
        return 0
    
    mid = (right + left) // 2

    if arr[mid] < num_to_find:
        return binary_search(arr, num_to_find, mid+1, right)
    elif arr[mid] > num_to_find:
        return binary_search(arr, num_to_find, left, mid-1)
    else:
        return 1

for n in input().split():
    print(binary_search(arr, int(n), 0, len(arr)-1))

# ------------------------------

input = __import__("sys").stdin.readline

N = int(input())
s = set(map(int, input().split()))
input()

for n in input().split():
    print(int(int(n) in s))