import heapq
import sys

min_heap = []
for i in range(int(sys.stdin.readline())):
    id = int(sys.stdin.readline())

    if id == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)

    else:
        heapq.heappush(min_heap, id)
