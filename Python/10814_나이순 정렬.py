import sys

# python의 내장함수는 안정 정렬 (같은 녀석들의 순서가 바뀌지 않음)
# key=lambda x: (int(x[0]), data.index(x))로 하는 경우 시간이 초과됨을 확인
input()
data = [info.split() for info in sys.stdin.read().rstrip().split('\n')]
for datum in sorted(data, key=lambda x: int(x[0])):
    print(*datum)

# -----------------------------

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
            if arr[left][0] <= arr[right][0]:
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
client_list = []
for _ in range(int(input())):
    age, name = input().split()
    client_list.append((int(age), name))

merge_sort(client_list)

for age, name in client_list:
    print(age, name)