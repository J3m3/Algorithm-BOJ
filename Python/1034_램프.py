input = __import__("sys").stdin.readline

# unique한 행들의 모양들이 있을 것.
# 각 모양별로 반복을 해야 함.
# 단 1번의 스위치 클릭 횟수만으로 특정 행이 밝아지기 위해서는, 그 행의 모양이 같아야 할 수밖에 없음.
# 따라서 각 행의 모양들을 기록하면서, K번의 스위치 클릭만으로 그 모양을 전체 on으로 바꿀 수 있는지를 생각해봐야 함.
# 바꿀 수 있다면, "그 모양의 수"만큼 행이 켜지게 될 것.
# 결국 전체 모양들을 반복하면서, 가장 큰 횟수를 출력하면 됨.

def count_zeros(shape):
    zero_count = 0
    for lamp in shape:
        if lamp == '0':
            zero_count += 1
    return zero_count

def can_row_on(zero_cnt):
    return zero_cnt <= K and (K + zero_cnt) % 2 == 0

N, M = map(int, input().split())

unique_shape = {}
for _ in range(N):
    shape = input().rstrip()

    if shape in unique_shape:
        unique_shape[shape][0] += 1
        continue

    unique_shape[shape] = [1, count_zeros(shape)]

K = int(input())

result = 0
for unique_shape_cnt, zero_cnt in unique_shape.values():
    if can_row_on(zero_cnt):
        result = max(result, unique_shape_cnt)

print(result)