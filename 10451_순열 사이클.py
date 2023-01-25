input = __import__("sys").stdin.readline

T = int(input())

for _ in range(T):
    count = 0  
    visited = {}
    size = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, size+1):
        if i not in visited:
            visited.setdefault(i)
            count += 1
        
            tmp = i
            while i != (next := arr[tmp-1]):
                tmp = next
                visited.setdefault(next)

    print(count)