# SEASON SPECIFIC

from tools import filter

cargo = {'auto': [7, 8], 'teleop': [10, 11]}

# Calculates the average auto/teleop points a team scores
def avg_cargo_points(arr, team, team_index, phase):
    m_array = filter.team(arr, team, team_index)
    m_upper = 0
    m_lower = 0
    # sum of cargo
    for m in range(len(m_array)):
        m_upper = m_upper + m_array[m][cargo[phase][0]]
        m_lower = m_lower + m_array[m][cargo[phase][1]]
    # calculating points
    if phase == 'auto':
        m_upper = m_upper * 4 # Points multiplier
        m_lower = m_lower * 2
    if phase == 'teleop':
        m_upper = m_upper * 2
        m_lower = m_lower * 1
    m_sum = m_upper + m_lower # sum of points
    m_avg = int(m_sum/len(m_array)) # average of points
    return m_avg

# Calulates the auto/teleop points a team scored in a particular match
def cargo_points(arr, team, team_index, phase):
    m_array = filter.team(arr, team, team_index)
    m_upper = m_array[0][cargo[phase][0]]
    m_lower = m_array[0][cargo[phase][1]]
    if phase == 'auto':
        m_upper = m_upper * 4 # Points multiplier
        m_lower = m_lower * 2
    if phase == 'teleop':
        m_upper = m_upper * 2
        m_lower = m_lower * 1
    return m_upper + m_lower