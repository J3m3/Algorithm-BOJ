def l_bound(arr, l, r, target):
    if l >= r:
        return r

    mid = (l + r) // 2

    if target > arr[mid]:
        return l_bound(arr, mid+1, r, target)
    
    else:
        return l_bound(arr, l, mid, target)


input = __import__("sys").stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lis_len = [arr[0]]

for num in arr:
    if num == lis_len[-1]:
        continue

    if num > lis_len[-1]:
        lis_len.append(num)
    
    else:
        idx = l_bound(lis_len, 0, len(lis_len), num)
        lis_len[idx] = num

print(len(lis_len))