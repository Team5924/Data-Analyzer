from tools import filter

cargo_indexes = [10, 11]
climb_index = 13

# 'indexes' is a list[]
# 2022 Rapid React Specific
def avg_cargo(arr, team, column):
    m_team = filter.team(arr, team, column)
    m_upper_sum = 0
    m_lower_sum = 0
    x = 0
    # Sum of points
    for m in range(len(m_team)):
        m_upper_sum = m_upper_sum + m_team[m][cargo_indexes[0]]
        m_lower_sum = m_lower_sum + m_team[m][cargo_indexes[1]]
        x = x + 1
    # Average points
    m_points = m_upper_sum + m_lower_sum
    return m_points