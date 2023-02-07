input = __import__("sys").stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()
left = count = 0
right = n - 1
total = arr[0] + arr[-1]

while left < right:
    if total >= target:
        if total == target:
            count += 1
        
        total -= arr[right]
        right -= 1
        total += arr[right]
    
    else:
        total -= arr[left]
        left += 1
        total += arr[left]

print(count)

# --------------------------------

input = __import__("sys").stdin.readline
MAX = 1000000

n = int(input())
arr = list(map(int, input().split()))
target = int(input())
needed = [0] * (2*MAX+1)
count = 0

for num in arr:
    if needed[num]:
        count += 1

    needed[target - num] = 1

print(count)