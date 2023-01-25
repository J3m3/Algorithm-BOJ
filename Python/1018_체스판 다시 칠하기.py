import sys

nrow, ncol = map(int, input().split())
chess = "WB" * 4
board = sys.stdin.read().split()

case_1 = []
case_2 = []
for i in range(ncol - len(chess) + 1):
    for j in range(nrow - len(chess) + 1):
        cnt_1 = 0
        cnt_2 = 0
        for line in [line[i:i+8] for line in board][j:j+8]:
            for idx, c in enumerate(line):
                if chess[idx] != line[idx]:
                    cnt_1 += 1
                if chess[::-1][idx] != line[idx]:
                    cnt_2 += 1

            chess = chess[::-1]

        case_1.append(cnt_1)
        case_2.append(cnt_2)

print(min(min(case_1), min(case_2)))