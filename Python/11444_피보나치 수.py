def multiply(A, B):
    length = len(A)
    result = [[0, 0], [0, 0]]
    for r in range(length):
        for c in range(length):
            total = 0
            for i in range(length):
                total += A[r][i] * B[i][c]
            
            result[r][c] = total % 1_000_000_007

    return result

def power(M, N):
    if N == 1:
        return M
    
    p = power(M, N // 2)
    result = multiply(p, p)

    if N & 1:
        result = multiply(result, M)
    
    return result

def fib(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    
    M = power([[1, 1], [1, 0]], N-1)
    return M[0][0]

input = __import__("sys").stdin.readline

print(fib(int(input())))