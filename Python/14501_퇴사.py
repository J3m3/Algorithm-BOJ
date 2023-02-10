input = __import__("sys").stdin.readline

N = int(input())

T_list = []
P_list = []
for i in range(N):
    t, p = map(int, input().split())
    T_list.append(t)
    P_list.append(p)

T_list += [0]
P_list += [0]
dp = P_list.copy()
for i in range(N):
    # 지금 날짜 + 상담에 걸리는 시간의 값을 update
    # i = 지금 날짜
    # i + T_list[i] = 지금 날짜 + 상담에 걸리는 시간
    # 우선 dp 배열을 P_list 값으로 초기화

    # dp[i + T_list[i]] = [지금 날짜 + 상담에 걸리는 시간]만큼이 지난 날짜의 가격
    # dp[i + T_list[i]] ~ dp[N]을 매번 반복하면서,
    # 그 날짜에 지금 할당된 가격이 [이전 것 + 기본 가격]보다 작으면 갱신
    # dp[i + T_list[i]] = max(dp[i + T_list[i]], dp[i] + P_list[i])

    # T[퇴사날] == 1이어도 그 날까진 근무 가능
    # 전 과정 반복하면 dp[N]에 가능한 최댓값이 기록

    for j in range(i + T_list[i], N+1):
        dp[j] = max(dp[j], dp[i] + P_list[j])


print(dp[-1])