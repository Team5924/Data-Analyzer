import numpy as np
import pandas as pd
from packages.Analyzer.modules import process, calculate
from modules.teams import teams_list
from IPython.display import Image
pd.set_option('display.max_columns', 100)

class Team():
    def __init__(this, data) -> None:
        this.data = data

    # Returns the raw data as a pandas DataFrame; really only useful for debugging
    def display(this):
        df = pd.DataFrame(this.data)
        return df
    
    # # Returns the metadata of a specific team
    # def metadata(this, team: int) -> pd.DataFrame:
    #     m_list = []
    #     labels = [
    #         'iD', 'Match', 'Attendance', 'Status', 'Defense', 'Sabotage', 'Notes'
    #     ]
    #     for entry in this.data:
    #         if entry['team'] == team:
    #             m_list.append([
    #                 process.id(entry['id']),
    #                 entry['match'],
    #                 process.binary(entry['attendance']),
    #                 entry['status'],
    #                 process.defense(entry['defense']),
    #                 process.binary(entry['sabotage']),
    #                 entry['notes'],

    #             ])

    #     df = pd.DataFrame(m_list, columns=labels)
    #     df.index += 1
    #     return df

    # Returns the name and image of the specific team
    def overview(this, team_num: int) -> any:
        file = 'modules/images/' + str(team_num) + '.jpg'
        for team in teams_list:
            if team[0] == team_num:
                print(team_num, team[1])
                
        return Image(filename=file, width=250)
    
    # Returns match data of a specific team
    def match(this, team: int) -> pd.DataFrame:
        m_list = []
        labels = [
            [''] * 3 + ['Auto'] * 3 + ['Score (Auto)'] * 3 + ['Score (Teleop)'] * 3 + ['Teleop'] * 5 + ['Endgame'] * 3 + ['Misc'],
            ['iD', 'Match', 'Attendance', 'Mobility', 'Docked', 'Engaged', 'Top', 'Mid', 'Bot', 'Top', 'Mid', 'Bot', 'Links', 'Pieces Dropped', 'Status', 'Defense', 'Sabotage', 'Parked', 'Docked', 'Engaged', 'Notes']
        ]
        for entry in this.data:
            if entry['team'] == team:
                m_list.append([
                    # ''
                    process.id(entry['id']),
                    entry['match'],
                    process.binary(entry['attendance']),
                    # 'Auto'
                    process.binary(entry['mobility']),
                    process.binary(entry['autoDocked']),
                    process.binary(entry['autoEngaged']),
                    # 'Score (Auto)'
                    calculate.row_score(entry, 'autoScore', 'top'),
                    calculate.row_score(entry, 'autoScore', 'mid'),
                    calculate.row_score(entry, 'autoScore', 'bot'),
                    # 'Score (Teleop)'
                    calculate.row_score(entry, 'teleopScore', 'top'),
                    calculate.row_score(entry, 'teleopScore', 'mid'),
                    calculate.row_score(entry, 'teleopScore', 'bot'),
                    # 'Teleop'
                    entry['links'],
                    entry['piecesDropped'],
                    entry['status'],
                    process.defense(entry['defense']),
                    process.binary(entry['sabotage']),
                    # 'Endgame'
                    process.binary(entry['parked']),
                    process.binary(entry['endgameDocked']),
                    process.binary(entry['endgameEngaged']),
                    # 'Misc'
                    entry['notes']
                ])
        
        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df