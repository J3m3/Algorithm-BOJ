input = __import__("sys").stdin.readline

def return_lis_map(arr):
    result = [1] * len(arr)
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                result[i] = max(result[i], result[j]+1)
    return result


def return_reverse_lis_map(arr):
    result = [1] * len(arr)
    for i in range(N, -1, -1):
        for j in range(i, N):
            if arr[i] > arr[j]:
                result[i] = max(result[i], result[j]+1)
    return result


N = int(input())
arr = list(map(int, input().split()))

lis_map = return_lis_map(arr)
rev_lis_map = return_reverse_lis_map(arr)

result = 0
for i in range(N):
    result = max(
        result,
        lis_map[i] + rev_lis_map[i] - 1
    )
print(result)