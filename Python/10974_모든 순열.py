input = __import__("sys").stdin.readline

N = int(input())
visited = [False] * (N+1)

def dfs(arr):
    if len(arr) == N:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(arr)
            arr.pop()
            visited[i] = False

dfs([])

# -----------------------

input = __import__("sys").stdin.readline
N = int(input())

def permute(nums):
    visited = [False] * (len(nums) + 1)
    permutation = []
    stack = [-1]
    # start recursion
    while stack:
        # -1 is only popped when inner while loop breaks || in the beginning
        idx = stack.pop() + 1
        while idx < len(nums):
            if not visited[nums[idx]]:
                # break to go down and push nums[idx] to permutation array
                break
            idx += 1
        else:
            # this block executed when...
            # 1. initial popped idx == -1 && all the numbers are visited
            # 2. initial popped idx == len(nums) (which means nums[idx] raises IndexError)
            if permutation:
                visited[permutation.pop()] = False
            # continue to reach the "next(in perspective of permutation, not natural order)" idx to iterate
            continue

        # save the current idx, the recursive state
        stack.append(idx)
        # push -1 to iterate range(1, len(nums))
        stack.append(-1)
        # form the next permutation array
        permutation.append(nums[idx])
        visited[nums[idx]] = True

        # base case
        if len(permutation) == len(nums):
            print(*permutation)

permute(list(range(1, N+1)))