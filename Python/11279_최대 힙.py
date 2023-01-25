import math
import sys


def remove_max(max_heap: list):
    if len(max_heap) == 0:
        return 0

    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    result = max_heap.pop()

    checker = True
    current_idx = 0

    while checker:
        left_idx = 2 * current_idx + 1
        right_idx = 2 * current_idx + 2

        if right_idx < len(max_heap):
            child_idx = left_idx if max_heap[left_idx] > max_heap[right_idx] else right_idx
        else:
            child_idx = left_idx

        if child_idx > len(max_heap) - 1:
            checker = False
        else:
            if max_heap[current_idx] < max_heap[child_idx]:
                max_heap[child_idx], max_heap[current_idx] = max_heap[current_idx], max_heap[child_idx]
                current_idx = child_idx
            else:
                checker = False

    return result


def add(max_heap: list, n: int):
    max_heap.append(n)

    checker = True
    current_idx = len(max_heap) - 1

    while checker:
        parent_idx = math.floor((current_idx - 1) / 2)
        if parent_idx < 0:
            checker = False
        else:
            if max_heap[parent_idx] < max_heap[current_idx]:
                max_heap[parent_idx], max_heap[current_idx] = max_heap[current_idx], max_heap[parent_idx]
                current_idx = parent_idx
            else:
                checker = False


def operation(max_heap: list, id: int):
    if (id == 0):
        return remove_max(max_heap)

    else:
        add(max_heap, id)


N = int(sys.stdin.readline())
max_heap = []

for i in range(N):
    result = operation(max_heap, int(sys.stdin.readline()))
    if result is not None:
        print(result)
