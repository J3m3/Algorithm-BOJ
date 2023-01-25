# stairs: [10, 20, 15, 25, 10, 20]
"""Bottom-Up"""
# dp: [10, 0, 0, 0, 0, 0]
# dp: [10, 30, 25, 0, 0, 0] ...

'''
점화식: 
    [목표 계단의 상대적 위치를 N이라고 가정]

    dp[N] = dp[N-3] + dp[N-1] + stairs[N] 
            
            OR

          = dp[N-2] + stairs[N]
    
    둘 중 최댓값 저장
'''

input = __import__("sys").stdin.readline

num_of_stairs = int(input())
stairs = [int(input()) for _ in range(num_of_stairs)]

# if len(stairs) <= 2:
#     print(sum(stairs))
# else:
#     dp = [0] * num_of_stairs
#     dp[0], dp[1], dp[2] = stairs[0], stairs[0] + stairs[1], stairs[0] + stairs[2]

#     for i in range(3, num_of_stairs):
#         dp[i] = max(
#             dp[i-3] + stairs[i-1] + stairs[i], 
#             dp[i-2] + stairs[i]
#         )

#     print(dp[-1])

if len(stairs) <= 2:
    c = sum(stairs)
else:
    a, b = stairs[0], stairs[0] + stairs[1]
    c = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, num_of_stairs):
        a, b, c = b, c, max(a + stairs[i-1] + stairs[i], b + stairs[i])

print(c)


'''
DP의 핵심
    1. 마지막 레벨에서 경우의 수 생각
    2. 점화식 도출
    3. 공간 복잡도 생각
'''

"""
dp 문제의 핵심은

1. 마지막 레벨에서 점화식 = 재귀적 규칙을 도출
2. 마지막 레벨까지의 list에 재귀적인 값들을 기억하고, 재사용
3. 이전 t개의 값만 필요한 경우, 굳이 list 만들지 않고도 ㄱㄴ
"""