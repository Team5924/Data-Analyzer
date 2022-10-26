import numpy as np
import pandas as pd

from tools import calculate

def team(arr, team_1, team_2, column):
    points_1 = calculate.avg_cargo(arr, team_1, column)
    points_2 = calculate.avg_cargo(arr, team_2, column)
    m_array = {"Team": [team_1, team_2], "Total Average Points": [points_1, points_2]}
    print(pd.DataFrame(m_array))

