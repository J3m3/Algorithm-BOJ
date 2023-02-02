input = __import__("sys").stdin.readline

N = int(input())
whole = set(range(N))
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')

def calculate_ability(team):
    total_ability = 0
    for i in team:
        for j in team:
            if i == j:
                continue
            total_ability += S[i][j]
    
    return total_ability


def calculate_ability_diff(team):
    remainder_team = whole - team

    team_link = calculate_ability(team)
    team_start = calculate_ability(remainder_team)

    return abs(team_link - team_start)


def dfs(team: set, start):
    if len(team) == N // 2:
        diff = calculate_ability_diff(team)
        global min_diff
        min_diff = min(min_diff, diff)
        return
    
    for i in range(start, N):
        team.add(i)
        dfs(team, i+1)
        team.discard(i)

dfs(set(), 0)
print(min_diff)