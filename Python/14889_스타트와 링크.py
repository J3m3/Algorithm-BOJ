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

# --------------------------

input = __import__("sys").stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = float('inf')
visited = [False] * N


def calculate_ability_diff():
    team_link = 0
    team_start = 0

    # Using 'in' with set is much more slower than accessing through indicies
    # Also, nested for loop for each team is slightly faster!
    # nested for loop for each team: 10^2 + 10^2 = 200 when N == 20
    # nested for loop like below (just one nested for loop): (20 * 21) / 2 = 210 when N == 20
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] and visited[j]:
                team_link += S[i][j] + S[j][i]

            elif not visited[i] and not visited[j]:
                team_start += S[i][j] + S[j][i]

    return abs(team_link - team_start)


def dfs(depth, start):
    if depth == N // 2:
        diff = calculate_ability_diff()
        global min_diff
        min_diff = min(min_diff, diff)
        return
    
    for i in range(start, N):
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False

dfs(0, 0)
print(min_diff)