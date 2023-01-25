n = int(input())
a, b = 0, 1; mod = 1000000
n %= 15 * mod // 10

for _ in range(n):
    a, b = b % mod, (a+b) % mod

print(a)

# ---------------------

