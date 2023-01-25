T = int(input())

# 파스칼 삼각형
from math import factorial
for _ in range(T):
    k = int(input())
    n = int(input())

    print(factorial(k+n) // (factorial(k+1) * factorial(n-1)))

# 동적 계획법 및 메모이제이션
for _ in range(T):
    k = int(input())
    n = int(input())

    floor = [i for i in range(1, n+1)]
   
    for _ in range(k):
        for i in range(1, n):
            floor[i] += floor[i-1]
    
    print(floor[-1])