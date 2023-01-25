def merge_sort(arr):
    def divide(l, r):
        if r - l < 2:
            return

        mid = (l + r) // 2
        divide(l, mid)
        divide(mid, r)

        merge(l, mid, r)

    def merge(l, mid, r):
        temp = []
        tail = r
        left, right = l, mid

        while left < mid and right < tail:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left < mid:
            temp.append(arr[left])
            left += 1
        while right < tail:
            temp.append(arr[right])
            right += 1
        
        for i in range(l, tail):
            arr[i] = temp[i-l]

    return divide(0, len(arr))

input = __import__("sys").stdin.readline
num_list = [int(input()) for _ in range(int(input()))]

merge_sort(num_list)

print(*num_list, sep='\n')