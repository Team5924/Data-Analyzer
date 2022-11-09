from tools import filter

# retrives the alliance color of a team during a specific match
def alliance(arr, team, team_index, match, match_index):
    m_array = filter.team(arr, team, team_index)
    for i in range(len(m_array)):
        if m_array[i][match_index] == match:
            return m_array[i][3] # '3' is the index of alliance