import sys

T = int(input())
for _ in range(T):
    ps = sys.stdin.readline().rstrip()

    while "()" in ps:
        ps = ps.replace("()", "")

    if ps:
        print("NO")
    else:
        print("YES")