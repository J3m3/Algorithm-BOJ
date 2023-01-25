import sys

def bubble(l: list):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
    return l

input()
for n in bubble(list(map(int, sys.stdin.read().split()))):
    print(n)