import sys

length = int(sys.stdin.readline())
nums = [0] * 10001

for _ in range(length):
    nums[int(sys.stdin.readline())] += 1

for idx in range(len(nums)):
    if nums[idx] != 0:
        for _ in range(nums[idx]):
            print(idx)