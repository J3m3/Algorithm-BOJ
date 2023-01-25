import sys

input()
nums = sorted(list(map(int, sys.stdin.read().split())))
modes = {}
for num in nums:
    modes[num] = modes.get(num, 0) + 1

keys = []
for key in modes:
    if modes[key] == max(modes.values()):
        keys.append(key)

print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])
print(sorted(keys)[1] if len(keys) != 1 else keys[0])
print(nums[-1] - nums[0])