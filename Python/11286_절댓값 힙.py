import heapq
import sys

abs_min_heap = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        if abs_min_heap:
            print(heapq.heappop(abs_min_heap)[-1])
        else:
            print(0)
    else:
        # tuple의 크기 비교는 첫 번째 원소에 대해서 진행. 만약 같다면 두 번째로, 또 같다면 세 번쨰...
        heapq.heappush(abs_min_heap, (abs(num), num))
