def prev_permutation(arr: list):
    left = -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            left = i
    
    if left < 0:
        return [left]
    
    for i in range(left+1, len(arr)):
        if arr[left] > arr[i]:
            right = i
    
    arr[left], arr[right] = arr[right], arr[left]
    arr = arr[:left+1] + list(reversed(arr[left+1:]))
    return arr

input = __import__("sys").stdin.readline

input()
print(*prev_permutation(list(map(int, input().split()))))