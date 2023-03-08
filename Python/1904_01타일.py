input = __import__("sys").stdin.readline

N = int(input())
'''
dp: 특정 시점 t에 가능한 모든 경우를 고려해 최적의 값을 찾은 후, 그 값을 다음에 다시 활용.
'''
a, b = 1, 2
for _ in range(N - 1):
    b, a = (a + b) % 15746, b

print(a)
