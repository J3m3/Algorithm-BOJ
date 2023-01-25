def count(N, row, col):
    if N == 0:
        return 0
    
    move_in_window = (2 * (row % 2)) + col % 2
    return move_in_window + 4 * count(N-1, row // 2, col // 2)


input = __import__("sys").stdin.readline
N, r, c = map(int, input().split())

print(count(N, r, c))