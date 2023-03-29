import numpy as np
import pandas as pd
from packages.Analyzer.modules import calculate
pd.set_option('display.max_columns', 100)

class Stats:
    def __init__(this, data) -> None:
        this.data = data

    # Returns the average stats w/ total average points of the given teams
    def averages(this, teams: list) -> pd.DataFrame:
        m_list = []
        labels = [
            [''] * 2 + ['Avg Auto Stats'] * 3 + ['Avg Points (Auto)'] * 3 + ['Avg Points (Teleop)'] * 3 + ['Avg Teleop Stats'] * 3 + ['Avg Endgame Stats'] * 3 + ['Misc'] * 2,
            [
                # ''
                'Team', 'Total Avg Points',
                # Avg Auto Stats
                'Mobility', 'Docked', 'Engaged',
                # Avg Points (Auto)
                'Top', 'Mid', 'Bot',
                # Avg Points (Telop)
                'Top', 'Mid', 'Bot',
                # Avg Teleop Stats
                'Links', 'Defense', 'Sabotage',
                # Avg Endgame Stats
                'Parked', 'Docked', 'Engaged',
                # Misc
                'Cones', 'Cubes'
            ]
        ]
        for team in teams:
            m_list.append([
                # '',
                team,
                calculate.total_avg_points(this.data, team),
                # 'Avg Auto Stats'
                calculate.avg_rate(this.data, team, 'mobility', 1),
                calculate.avg_rate(this.data, team, 'autoDocked', 1),
                calculate.avg_rate(this.data, team, 'autoEngaged', 1),
                # 'Avg Points (Auto)'
                calculate.avg_row_points(this.data, team, 'autoScore', 'top', 6),
                calculate.avg_row_points(this.data, team, 'autoScore', 'mid', 4),
                calculate.avg_row_points(this.data, team, 'autoScore', 'bot', 3),
                # 'Avg Points (Teleop)'
                calculate.avg_row_points(this.data, team, 'teleopScore', 'top', 5),
                calculate.avg_row_points(this.data, team, 'teleopScore', 'mid', 3),
                calculate.avg_row_points(this.data, team, 'teleopScore', 'bot', 2),
                # 'Avg Teleop Stats'
                calculate.avg_value(this.data, team, 'links'),
                calculate.avg_defense(this.data, team),
                calculate.avg_rate(this.data, team, 'sabotage', 1),
                # 'Avg Endgame Stats'
                calculate.avg_rate(this.data, team, 'parked', 1),
                calculate.avg_rate(this.data, team, 'endgameDocked', 1),
                calculate.avg_rate(this.data, team, 'endgameEngaged', 1),
                # 'Misc'
                calculate.cone_rate(this.data, team),
                calculate.cube_rate(this.data, team),
            ])

        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df
    
    # Returns the average stats w/ total average points (weighted) of the given teams:
    def weighted_averages(this, teams: list, weights: list) -> pd.DataFrame:
        m_list = []
        labels = [
            [''] * 2 + ['Avg Auto Stats'] * 3 + ['Avg Points (Auto)'] * 3 + ['Avg Points (Teleop)'] * 3 + ['Avg Teleop Stats'] * 3 + ['Avg Endgame Stats'] * 3 + ['Misc'] * 2,
            [
                # ''
                'Team', 'Total Avg Points (Weighted)',
                # Avg Auto Stats
                'Mobility', 'Docked', 'Engaged',
                # Avg Points (Auto)
                'Top', 'Mid', 'Bot',
                # Avg Points (Telop)
                'Top', 'Mid', 'Bot',
                # Avg Teleop Stats
                'Links', 'Defense', 'Sabotage',
                # Avg Endgame Stats
                'Parked', 'Docked', 'Engaged',
                # 'Misc'
                'Cones', 'Cubes'
            ]
        ]
        for team in teams:
            m_list.append([
                # '',
                team,
                calculate.weighted_avg_points(this.data, team, weights),
                # 'Avg Auto Stats'
                calculate.avg_rate(this.data, team, 'mobility', 1),
                calculate.avg_rate(this.data, team, 'autoDocked', 1),
                calculate.avg_rate(this.data, team, 'autoEngaged', 1),
                # 'Avg Points (Auto)'
                calculate.avg_row_points(this.data, team, 'autoScore', 'top', 6),
                calculate.avg_row_points(this.data, team, 'autoScore', 'mid', 4),
                calculate.avg_row_points(this.data, team, 'autoScore', 'bot', 3),
                # 'Avg Points (Teleop)'
                calculate.avg_row_points(this.data, team, 'teleopScore', 'top', 5),
                calculate.avg_row_points(this.data, team, 'teleopScore', 'mid', 3),
                calculate.avg_row_points(this.data, team, 'teleopScore', 'bot', 2),
                # 'Avg Teleop Stats'
                calculate.avg_value(this.data, team, 'links'),
                calculate.avg_defense(this.data, team),
                calculate.avg_rate(this.data, team, 'sabotage', 1),
                # 'Avg Endgame Stats'
                calculate.avg_rate(this.data, team, 'parked', 1),
                calculate.avg_rate(this.data, team, 'endgameDocked', 1),
                calculate.avg_rate(this.data, team, 'endgameEngaged', 1),
                # 'Misc'
                calculate.cone_rate(this.data, team),
                calculate.cube_rate(this.data, team),
            ])

        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df
    
