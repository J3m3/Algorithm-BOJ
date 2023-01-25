input = __import__("sys").stdin.readline

for _ in range(int(input())):
    a, b, c = [1, 1, 1]
    N = int(input())

    for _ in range(N-3):
        a, b, c = b, c, a+b
    
    print(c)