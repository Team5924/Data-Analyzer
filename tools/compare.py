import numpy as np
import pandas as pd

from tools import calculate

def team(arr, num_teams):
    # save a list teams to compare
    teams = []
    for i in range(num_teams):
        teams.append([int(input("Enter a team:"))])
    # Finds the average points for each team
    for m in range(len(teams)):
        teams[m].append(calculate.avg_cargo_points(arr, teams[m][0], 4, "auto"))
        teams[m].append(calculate.avg_cargo_points(arr, teams[m][0], 4, "teleop"))
    return teams