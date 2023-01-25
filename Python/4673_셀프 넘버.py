def d(n):
    return n + sum(map(int, list(str(n))))

s = set(range(1, 10001))
pop = set()

# 9973
for n in range(1, 10000):
    pop.add(d(n))

for num in sorted(list(s - pop)):
    print(num)