X = int(input())

n = 1
count = 1
while X > n:
    count += 1
    n += count

s = [str(X - (n - count)), '/', str(n - X + 1)]
if count % 2 == 0:
    print("".join(s))
else:
    print("".join(s[::-1]))