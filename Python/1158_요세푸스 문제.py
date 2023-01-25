from collections import deque

n, k = map(int, input().split())
members = deque(range(1, n+1))
result = []

for _ in range(n):
    members.rotate(-k)
    result.append(str(members.pop()))

print(f"<{', '.join(result)}>")

'''
--------------------------------------------------
'''

# idx = k - 1
# for i in range(n):
#     if len(members) <= idx:
#         idx %= len(members)
#     result.append(str(members.pop(idx)))
#     idx += k - 1

# print(f"<{', '.join(result)}>")