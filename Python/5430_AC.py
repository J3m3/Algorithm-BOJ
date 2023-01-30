from collections import deque
input == __import__("sys").stdin.readline

for _ in range(int(input())):
    cmds = input().rstrip()
    N = int(input())
    nums_s = input()[1:-1].split(',')
    deq = deque(nums_s) if N else deque()

    reverse_count = 0
    for cmd in cmds:
        if cmd == 'R':
            reverse_count += 1
        
        else:
            if deq:
                if reverse_count & 1:
                    deq.pop()
                else:
                    deq.popleft()
            else:
                print("error")
                break
    else:
        if reverse_count & 1:
            deq.reverse()
        print(f"[{','.join(deq)}]")
