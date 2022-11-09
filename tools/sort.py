import re


m_type = {"team": 0, "auto": 1, "teleop": 2}

# generic sorting funciton
def order(arr, type, direction):
    m_arr = []
    order = []
    for i in range(len(arr)):
        # records the team # and it's index
        m_arr.append([arr[i][m_type[type]], i]) # arr[i][0] = teams
    # sorts the teams from least to greatest
    m_arr.sort(reverse=direction)
    # stores the order of the indexes 'teams'
    for i in range(len(m_arr)):
        order.append(m_arr[i][1])
    # reorganizes 'teams' in correspondence to 'order'
    for i in range(len(arr)):
        m_arr[i] = arr[order[i]]
    return m_arr

# Groups alliance colors together and improves visualization
def alliance(arr):
    alliance = []
    order = []
    red = []
    blue = []
    for i in range(len(arr)):
        # records the team # and it's index
        if arr[i][1] == "Red": # '1' is the alliance index
            alliance.append([0, i])
        if arr[i][1] == "Blue":
            alliance.append([1, i])
    # sorts the teams from least to greatest
    alliance.sort()
    # stores the order of the indexes 'teams'
    for i in range(len(arr)):
        order.append(alliance[i][1])
    # reorganizes 'teams' in correspondence to 'order'
    for i in range(len(arr)):
        alliance[i] = arr[order[i]]
    # formats array so that alliance is separated side by side
    for i in range(int(len(arr)/2)):
        red.append(alliance[i])
        blue.append(alliance[-(i+1)]) # negative indexes start from the end of the array
    for i in range(len(red)):
        for j in range(len(blue[0])):
            red[i].append(blue[i][j]) # insert blue teams into between red teams
    alliance = red
    return alliance