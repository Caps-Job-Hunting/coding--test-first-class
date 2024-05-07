def calculate_ability(team, ability_matrix):
    ability = 0
    for i in team:
        for j in team:
            if i != j:
                ability += ability_matrix[i][j]
    return ability


def backtrack(index, current_team, ability_matrix, N, min_diff):
    if len(current_team) == N // 2:
        team_link = [i for i in range(N) if i not in current_team]
        ability_start = calculate_ability(current_team, ability_matrix)
        ability_link = calculate_ability(team_link, ability_matrix)
        current_diff = abs(ability_start - ability_link)
        min_diff[0] = min(min_diff[0], current_diff)
        return

    for i in range(index, N):
        current_team.append(i)
        backtrack(i + 1, current_team, ability_matrix, N, min_diff)
        current_team.pop()


min_diff = [float('inf')]
N = int(input())
ability_matrix = [list(map(int, input().split())) for _ in range(N)]

backtrack(0, [], ability_matrix, N, min_diff)

print(min_diff[0])
