def multiply(A, B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(N):
                total += A[i][k] * B[k][j]

            result[i][j] = total % 1000
    
    return result

def power(A, n):
    if n == 1:
        return A
    
    partial = power(A, n // 2)
    result = multiply(partial, partial)
    
    if n & 1:
        result = multiply(result, A)
    
    return result

input = __import__("sys").stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = power(A, B)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()