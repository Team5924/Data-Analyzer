from packages.Analyzer.modules import process

# Calculates the total PIECES scored in a row of a given phase
def row_score(entry: list, phase: str, row: str) -> int:
    return entry[phase][row]['cones'] + entry[phase][row]['cubes']

""" TOTALS """
# Calculate the total matches attended
def total_matches(data: list, team: int) -> int:
    matches = 0
    for entry in data:
        # only count if the team has participated in the match
        if entry['team'] == team and entry['attendance'] == 1:
            matches += 1

    return matches

# Calculates the total value of a specific field
def total_value(data: list, team: int, field: str) -> int:
    count = 0
    for entry in data:
        # only count if the team has participated in the match
        if entry['team'] == team and entry['attendance'] == 1:
            count += entry[field]
    return count

# Calculates the total pieces scored in a row of a given phase
def total_row_score(data: list, team: int, phase: str, row: str) -> int:
    score = 0
    for entry in data:
        if entry['team'] == team and entry['attendance'] == 1:
            score += row_score(entry, phase, row)

    return score

# Calculates the total points scored of a given phase
def total_phase_points(data: list, team: int, phase: str, multiplier: list) -> int:
    points = 0
    for entry in data:
        if entry['team'] == team and entry['attendance'] == 1:
            points += row_score(entry, phase, 'top') * multiplier[0]
            points += row_score(entry, phase, 'mid') * multiplier[1]
            points += row_score(entry, phase, 'bot') * multiplier[2]

    return points

# Calculates the total pieces a team scored
def total_pieces(data: list, team: int) -> int:
    pieces = 0
    for entry in data:
        if entry['team'] == team and entry['attendance'] == 1:
            pieces += row_score(entry, 'autoScore', 'top')
            pieces += row_score(entry, 'autoScore', 'mid')
            pieces += row_score(entry, 'autoScore', 'bot')
            pieces += row_score(entry, 'teleopScore', 'top')
            pieces += row_score(entry, 'teleopScore', 'mid')
            pieces += row_score(entry, 'teleopScore', 'bot')

    return pieces

# # Calculates the total occurence of a specific field
# def total_occurence(data: list, team: int, field: str, occurence: any) -> int:
#     count = 0
#     for entry in data:
#         if entry['team'] == team and entry['attendance'] == 1:
#             if entry[field] == occurence:
#                 count += 1

#     return count

""" AVERAGES """
# Calculates the average value of a specific field
def avg_value(data: list, team: int, field: str) -> float or str:
    try:
        avg_value = round(total_value(data, team, field) / total_matches(data, team), 2)
    except ZeroDivisionError:
        avg_value = 'N/A'
    return avg_value
            
# Calculates the average rate of occurence of a specific field
def avg_rate(data: list, team: int, field: str, occurence: any) -> str:
    avg_rate = str(round(total_value(data, team, field) / total_matches(data, team) * 100, 2)) + '%'
    return avg_rate

# Calculates the average POINTS scored in a row
def avg_row_points(data: list, team: int, phase:str, row: str, multiplier: int) -> float:
    avg_count = total_row_score(data, team, phase, row) / total_matches(data, team)
    avg_points = round(avg_count * multiplier, 2)
    return avg_points

# Calculates the average defense rating
def avg_defense(data: list, team: int) -> int:
    count = 0
    matches = 0
    for entry in data:
        if entry['team'] == team and entry['attendance'] == 1:
            if entry['defense'] != 'N/A':
                count += process.defense(entry['defense'])
                matches += 1

    try:
        avg_defense_rating = round(count / matches, 2)
    except ZeroDivisionError:
        avg_defense_rating = 'N/A'
    return avg_defense_rating

# Calculates the average total points scored by a team
def total_avg_points(data: list, team: int) -> int:
    mobility = total_value(data, team, 'mobility') * 3
    autoDocked = total_value(data, team, 'autoDocked') * 8
    autoEngaged = total_value(data, team, 'autoEngaged') * 4
    autoScore = total_phase_points(data, team, 'autoScore', [6, 4, 3])
    teleopScore = total_phase_points(data, team, 'teleopScore', [5, 3, 2])
    links = total_value(data, team, 'links') * 5
    parked = total_value(data, team, 'parked') * 2
    endgameDocked = total_value(data, team, 'endgameDocked') * 6
    endgameEngaged = total_value(data, team, 'endgameEngaged') * 4
    
    total_points = mobility + autoDocked + autoEngaged + autoScore + teleopScore + links + parked + endgameDocked + endgameEngaged
    avg_points = round(total_points / total_matches(data, team), 2)
    return avg_points

# Calculates the weighted average points scored by a team
def weighted_avg_points(data: list, team: int, weights: list) -> int:
    mobility = total_value(data, team, 'mobility') * 3 * weights[0]
    autoDocked = total_value(data, team, 'autoDocked') * 8 * weights[1]
    autoEngaged = total_value(data, team, 'autoEngaged') * 4 * weights[2]
    autoScore = total_phase_points(data, team, 'autoScore', [6 * weights[3][0], 4 * weights[3][1], 3 * weights[3][2]])
    teleopScore = total_phase_points(data, team, 'teleopScore', [5 * weights[4][0], 3 * weights[4][1], 2 * weights[4][2]])
    links = total_value(data, team, 'links') * 5 * weights[5]
    parked = total_value(data, team, 'parked') * 2 * weights[6]
    endgameDocked = total_value(data, team, 'endgameDocked') * 6 * weights[7]
    endgameEngaged = total_value(data, team, 'endgameEngaged') * 4 * weights[8]
    
    total_points = mobility + autoDocked + autoEngaged + autoScore + teleopScore + links + parked + endgameDocked + endgameEngaged
    avg_points = round(total_points / total_matches(data, team), 2)
    return avg_points

# Calculates the rate of cones scored by a team:
def cone_rate(data: list, team: int) -> int:
    cones = 0
    for entry in data:
        if entry['team'] == team:
            cones += entry['autoScore']['top']['cones']
            cones += entry['autoScore']['mid']['cones']
            cones += entry['autoScore']['bot']['cones']
            cones += entry['teleopScore']['top']['cones']
            cones += entry['teleopScore']['mid']['cones']
            cones += entry['teleopScore']['bot']['cones']

    return str(round(cones / total_pieces(data, team) * 100, 2)) + '%'

# Calculates the rate of cubes scored by a team:
def cube_rate(data: list, team: int) -> int:
    cubes = 0
    for entry in data:
        if entry['team'] == team:
            cubes += entry['autoScore']['top']['cubes']
            cubes += entry['autoScore']['mid']['cubes']
            cubes += entry['autoScore']['bot']['cubes']
            cubes += entry['teleopScore']['top']['cubes']
            cubes += entry['teleopScore']['mid']['cubes']
            cubes += entry['teleopScore']['bot']['cubes']

    return str(round(cubes / total_pieces(data, team) * 100, 2)) + '%'