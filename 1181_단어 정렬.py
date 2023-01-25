import sys

input()
for word in sorted(list(set(sys.stdin.read().split())), key=lambda x: (len(x), x)):
    print(word)