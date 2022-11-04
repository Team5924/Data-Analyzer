def team(arr):
    teams = []
    order = []
    for m in range(len(arr)):
        teams.append([arr[m][0], m])
    teams.sort()
    for m in range(len(teams)):
        order.append(teams[m][1])
    for m in range(len(arr)):
        teams[m] = (arr[order[m]])
    return teams
