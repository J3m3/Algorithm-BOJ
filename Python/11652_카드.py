input = __import__("sys").stdin.readline

num_map = {}
for _ in range(int(input())):
    n = int(input())
    num_map[n] = num_map.get(n, 0) + 1

max_idx = n # n is visible, by LEGB Rule
for k in num_map:
    if num_map[max_idx] < num_map[k]:
        max_idx = k
    
    elif num_map[max_idx] == num_map[k] and k < max_idx:
        max_idx = k

print(max_idx)