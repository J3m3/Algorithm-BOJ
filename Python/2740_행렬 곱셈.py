input = __import__("sys").stdin.readline

def multiply(A, B):
    result = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            total = 0
            for k in range(M):
                total += A[i][k] * B[k][j]
            
            result[i][j] = total
    
    return result

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = multiply(A, B)
for i in range(N):
    print(*result[i])