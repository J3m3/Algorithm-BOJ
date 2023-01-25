from sys import stdin

N, M = map(int, stdin.readline().split())

pokemons = {}
numbers = {}
for num in range(1, N+1):
    name = stdin.readline().rstrip()

    pokemons[num] = name
    numbers[name] = num

for _ in range(M):
    if (val := stdin.readline().rstrip()).isalpha():
        print(numbers[val])
    else:
        print(pokemons[int(val)])