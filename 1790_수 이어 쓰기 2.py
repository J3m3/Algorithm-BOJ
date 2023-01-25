input = __import__("sys").stdin.readline

N, k = map(int, input().split())

len_of_k = 1
nine = 9

while k > len_of_k * nine:
    k -= len_of_k * nine
    len_of_k += 1
    nine *= 10

answer = 10 ** (len_of_k - 1) + (k - 1) // len_of_k
print(str(answer)[(k-1) % len_of_k] if answer <= N else -1)