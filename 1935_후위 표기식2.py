import sys
from queue import Queue

N = int(sys.stdin.readline())
rep = sys.stdin.readline().rstrip()
operands = {chr(i+64):int(sys.stdin.readline()) for i in range(1, N+1)}

stack = []
for char in rep:
    # 후위표기식에서 연산자를 만나면,
    # 스택에 있는 계산된 정수 2개와 연산자를 빼서 eval하고
    # 다시 스택에 집어넣음
    if stack and char in "*+/-":
        b = stack.pop()
        a = stack.pop()
        result = eval(f"{a}{char}{b}")
        stack.append(f"{result:.2f}")

    # 후위표기식에서 피연산자를 만나면,
    # operands dict에서 정수를 하나 뽑아서
    # 스택에 집어넣음
    else:
        stack.append(operands[char])

print(*stack)