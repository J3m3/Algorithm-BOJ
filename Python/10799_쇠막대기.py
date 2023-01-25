# S = input().replace("()", "$")
# stack_p = []
# st_ed = []
# for idx in range(len(S)):
#     if S[idx] != "$":
#         stack_p.append((S[idx], idx))

#     if len(stack_p) >= 2:
#         if stack_p[-1][0] == ")" and stack_p[-2][0] == "(":
#             st_ed.append((stack_p[-2][1], stack_p[-1][1]))
#             stack_p.pop()
#             stack_p.pop()

# total = 0
# for start, end in st_ed:
#     total += S[start:end+1].count("$") + 1

# print(total)

stick = 0
total = 0
for c in input().replace("()", "$"):
    if c == "$":
        total += stick
    elif c == "(":
        stick += 1
    else:
        total += 1
        stick -= 1
    
print(total)