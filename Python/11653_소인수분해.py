N = int(input())

for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        N //= i
        print(i)
        
if N != 1:
    print(N)