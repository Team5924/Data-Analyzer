def team(arr):
    teams = []
    order = []
    for m in range(len(arr)):
        # records the index of each team #
        teams.append([arr[m][0], m])
    # sorts the teams from least to greatest
    teams.sort()
    # stores the order of the teams
    for m in range(len(teams)):
        order.append(teams[m][1])
    # replaces each index of 'teams' with an element of 'arr' based on the 'order'
    for m in range(len(arr)):
        teams[m] = (arr[order[m]])
    return teams
