input = __import__("sys").stdin.readline

# 투 포인터 알고리즘 for 양의 정수 배열의 연속된 구간합
N, M = map(int, input().split())

# 포인터가 index의 역할을 하기보단 구간의 상하한이기 때문에, len(arr)까지는 keyError 없이 허용되어야 함
# left == right일 때를 구간의 크기가 0일 때로 정의
# 따라서 arr[-1] 값을 포함하기 위해서 right는 MAX_IDX+1의 범위까지 포함할 수밖에 없음.
arr = list(map(int, input().split())) + [0]
left = right = count = total = 0

while right <= N:
    # 구간합이 M보다 크거나 같아지면 left를 오른쪽으로
    # 구간합이 M보다 작으면 right를 오른쪽으로
    
    if total >= M:
        # 같아질 때는 count++
        if total == M:
            count += 1

        total -= arr[left]
        left += 1

    else:
        total += arr[right]
        right += 1

print(count)

"""
-----------------------
"""

# 혹은 투 포인터 대신 right 포인터와 각 arr의 원소들 자체를 이용해 풀 수 있음
# 개인적으로 이해하기 훨씬 용이함
# !!!!!!!!!!!!!!! 매우 큰 문제점: right가 갱신되는 타이밍에 total == M을 검사할 수 없음
# 이 문제에서는 total == M이 아닌 경우는 따로 저장할 필요가 없지만,
# "25916_싫은데요"와 같이 만족하는 최댓값을 찾는 과정에서 max 값을 갱신해야 할 때는 사용할 수 없음
right = total = count = 0

for start in arr:
    while total < M and right < N:
        total += arr[right]
        right += 1
    
    if total == M:
        count += 1
    
    total -= start

print(count)