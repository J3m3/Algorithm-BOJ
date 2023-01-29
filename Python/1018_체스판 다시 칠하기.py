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

# -----------------------------------

input = __import__("sys").stdin.readline
N, M = map(int, input().split())

board = [input().rstrip() for _ in range(N)]
sample_1 = ['W', 'B']
sample_2 = ['B', 'W']

min_count = float('inf')
for y in range(N-7):
    for x in range(M-7):
        count_1 = 0
        count_2 = 0
        for i in range(y, y+8):
            for j in range(x, x+8):
                s = board[i][j]

                if s == sample_1[j & 1]:
                    count_1 += 1
                elif s == sample_2[j & 1]:
                    count_2 += 1

            sample_1.reverse()
            sample_2.reverse()

        if min_count > (count := min(count_1, count_2)):
            min_count = count

print(min_count)