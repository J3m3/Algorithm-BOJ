binary = input()
zeros = ''
if len(binary) % 3 == 1:
    zeros = '0' * 2
elif len(binary) % 3 == 2:
    zeros = '0'

binary = zeros + binary
length = len(binary)

result = ""
each_bin = 0
for idx in range(length):
    each_bin += int(binary[idx]) * 2 ** (-(idx % 3) + 2)

    if idx % 3 == 2:
        result += str(each_bin)
        each_bin = 0

print(result)