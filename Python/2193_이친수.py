input = __import__("sys").stdin.readline

'''
1
10
100, 101
1010, 1000, 1001
10100, 10101, 10010, 10000, 10001
'''

a, b = 1, 1
for _ in range(int(input())-1):
    b, a = a + b, b
print(a)
