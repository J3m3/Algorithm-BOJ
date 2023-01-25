N = int(input())

# q = N // 5
# while (N - 5 * q) % 3 != 0:
#     q -= 1
#     if q < 0:
#         result = -1
#         break
# else:
#     result = q + (N - 5 * q) // 3

count3 = 0
while N % 5 != 0:
    if N < 0:
        result = -1
        break
    N -= 3
    count3 += 1
else:
    result = (N // 5) + count3

print(result)
