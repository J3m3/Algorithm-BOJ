def next_permutation(arr):
    last_asc_idx = -1
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            last_asc_idx = i
    
    if last_asc_idx == -1:
        return [-1]
    
    for i in range(last_asc_idx+1, len(arr)):
        if arr[last_asc_idx] < arr[i]:
            # last_asc_idx는 마지막 오름차순인 부분에 위치하므로,
            # arr[last_asc_idx]보다 큰 임의의 arr[i]가 반드시 존재 (단, last_asc_idx < i)
            # python은 block scope가 따로 없음 (LEGB Rule)
            farthest_bigger_idx = i
    
    arr[last_asc_idx], arr[farthest_bigger_idx] = arr[farthest_bigger_idx], arr[last_asc_idx]
    arr = arr[:last_asc_idx+1] + list(reversed(arr[last_asc_idx+1:]))
    return arr

input = __import__("sys").stdin.readline
input()
print(*next_permutation(list(map(int, input().split()))))