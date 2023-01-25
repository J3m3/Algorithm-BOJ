N = int(input())

count = 0
for n in range(1, N+1):
    if len(str(n)) < 3:
        count += 1
    else:
        if (int(str(n)[0]) + int(str(n)[-1])) / 2 == sum([int(i) for i in str(n)]) / len(str(n)):
            count += 1

print(count)