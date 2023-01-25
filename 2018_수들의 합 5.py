"""
1
1+2
1+2+3
1+2+3+4
1+2+3+4+5
2+3+4+5
2+3+4+5+6
3+4+5+6
4+5+6
5+6
5+6+7
6+7
6+7+8
7+8
8
8+9
...
15
"""

input = __import__("sys").stdin.readline

# 배열 미리 생성해서 풀면 메모리 초과!!!
N = int(input())


total = 0
count = 0
dec = 1
inc = 1

while inc <= N+1:
    if total == N:
        count += 1
    
    if total >= N:
        total -= dec
        dec += 1
    
    else:
        total += inc
        inc += 1
        
print(count)