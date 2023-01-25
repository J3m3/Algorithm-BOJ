def hanoi(n, start, end, sub):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, sub, end)
    print(start, end)
    hanoi(n-1, sub, end, start)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3, 2)