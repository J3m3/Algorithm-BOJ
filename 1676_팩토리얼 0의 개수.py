def fac_zero_count(n):
    if n == 0:
        return 0

    else:
        fac = 1
        count = 0
        for n in range(2, n+1):
            fac *= n
            while fac % 5 == 0 and fac % 2 == 0:
                count += 1
                fac //= 10

        return count


print(fac_zero_count(int(input())))
