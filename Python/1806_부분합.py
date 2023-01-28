input = __import__("sys").stdin.readline

def size(l, r):
    return r - l

N, S = map(int, input().split())
arr = list(map(int, input().split())) + [0]

left = right = 0
total = 0
minimum_length = len(arr)

while right <= N:
    if total >= S:
        if minimum_length > (length := size(left, right)):
            minimum_length = length
    
        total -= arr[left]
        left += 1

    else:
        total += arr[right]
        right += 1

print(minimum_length if minimum_length != len(arr) else 0)