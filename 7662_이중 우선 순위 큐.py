import heapq
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    min_heap = []
    max_heap = []
    dic = {}

    k = int(sys.stdin.readline())

    for _ in range(k):
        commands = sys.stdin.readline().split()

        if commands[0] == "I":
            v = int(commands[1])
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, -v)
            dic[v] = dic.get(v, 0) + 1

        else:
            if min_heap and int(commands[1]) == -1:
                m = heapq.heappop(min_heap)
                dic[m] -= 1

            elif max_heap and int(commands[1]) == 1:
                M = -heapq.heappop(max_heap)
                dic[M] -= 1

            while min_heap and dic[min_heap[0]] <= 0:
                heapq.heappop(min_heap)
            while max_heap and dic[-max_heap[0]] <= 0:
                heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
