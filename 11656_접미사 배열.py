string = input()
suffixes = []

for i in range(len(string)):
    suffixes.append(string[i:])

for suffix in sorted(suffixes):
    print(suffix)