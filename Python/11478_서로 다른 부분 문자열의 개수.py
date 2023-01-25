input = __import__("sys").stdin.readline
s = input().rstrip()
Set = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        Set.add(s[i:j+1])

print(len(Set))