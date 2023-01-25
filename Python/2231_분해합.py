num = int(input())

for n in range(num-len(str(num))*9, num+1):
    if n <= 0:
        continue

    if n + sum(map(int, str(n))) == num:
        print(n)
        break
else:
    print(0)