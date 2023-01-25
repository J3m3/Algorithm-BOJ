input = __import__("sys").stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

def binary_search(arr, left, right, target):
    if left >= right:
        return right - 1
    
    mid = (left + right) // 2
    total_Q = 0
    for lan in arr:
        total_Q += lan // mid
    
    if total_Q < target:
        return binary_search(arr, left, mid, target)
    
    else:
        return binary_search(arr, mid+1, right, target)

print(binary_search(lans, 1, max(lans)+1, N))