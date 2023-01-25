input = __import__("sys").stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(trees, num_to_find, left, right):
    if left > right:
        return right
    
    mid = (left + right) // 2
    total = 0

    for n in trees:
        if mid < n:
            total += n - mid

    if num_to_find > total:
        return binary_search(trees, num_to_find, left, mid-1)
    
    elif num_to_find < total:
        return binary_search(trees, num_to_find, mid+1, right)
    
    else:
        return mid

Max = max(trees)
print(binary_search(trees, M, 0, Max))