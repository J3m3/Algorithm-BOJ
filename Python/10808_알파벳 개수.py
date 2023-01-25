from sys import stdin

alpha_map = {chr(ascii):0 for ascii in range(ord('a'), ord('z')+1)}
for char in stdin.readline().rstrip():
    alpha_map[char] = alpha_map.get(char, 0) + 1

print(*alpha_map.values())