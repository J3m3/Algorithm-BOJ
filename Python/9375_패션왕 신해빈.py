input = __import__("sys").stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    cloth_map = {}
    for _ in range(N):
        val, key = input().split()

        if key in cloth_map:
            cloth_map[key].append(val)

        else:
            cloth_map[key] = []
            cloth_map[key].append(val)

    # 같은 종류 내에서는 1개까지만
    # 전체 기준 적어도 1개
    # 각 cluster에서 나올 수 있는 경우의 수 = len(cluster) + 1 (1개 고르는 경우의 수 + 아무것도 고르지 않는 경우의 수)
    # 곱의 법칙에 따라 곱하고, 마지막에 전체 기준 아무것도 고르지 않은 경우를 제외 = total - 1
    total = 1
    for l in cloth_map.values():
        total *= len(l) + 1
    
    print(total - 1)