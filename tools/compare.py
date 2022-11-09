import numpy as np
import pandas as pd

from tools import filter, calculate, get

def team(arr, teams_list):
    # saves a list teams to compare
    teams = []
    for i in range(len(teams_list)):
        teams.append([teams_list[i]])
    # Finds the average points for each team
    for i in range(len(teams)):
        teams[i].append(calculate.avg_cargo_points(arr, teams[i][0], 4, "auto"))
        teams[i].append(calculate.avg_cargo_points(arr, teams[i][0], 4, "teleop"))
    return teams

def match(arr, match, match_index):
    # saves a list of teams
    m_array = filter.match(arr, match, match_index)
    teams = []
    for i in range(len(m_array)):
        teams.append([m_array[i][4]])
    # finds the alliance, auto and teleop points for each team
    for i in range(len(teams)):
        teams[i].append(get.alliance(arr, teams[i][0], 4, match, match_index))
        teams[i].append(calculate.cargo_points(m_array, teams[i][0], 4, "auto"))
        teams[i].append(calculate.cargo_points(m_array, teams[i][0], 4, "teleop"))
    return teams