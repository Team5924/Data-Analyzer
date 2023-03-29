import numpy as np
import pandas as pd
from modules.id import id_list
from packages.Analyzer.modules import process, calculate
pd.set_option('display.max_columns', 100)

class iD:
    def __init__(this, data) -> None:
        this.data = data

    def leaderboard(this) -> pd.DataFrame:
        m_list = []
        labels = [
            'iD', 'Count', 'Matches'
        ]
        for id in id_list:
            count = 0
            matches = []
            for entry in this.data:
                if id[0] == entry['id']:
                    count += 1
                    matches.append(entry['match'])
            m_list.append([
                process.id(id[0]),
                count,
                matches
            ])

        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df

    def lookup(this, id: int) -> pd.DataFrame:
        m_list = []
        labels = [
            [''] * 3 + ['Auto'] * 3 + ['Score (Auto)'] * 3 + ['Score (Teleop)'] * 3 + ['Teleop'] * 5 + ['Endgame'] * 3 + ['Misc'],
            ['Team', 'Match', 'Attendance', 'Mobility', 'Docked', 'Engaged', 'Top', 'Mid', 'Bot', 'Top', 'Mid', 'Bot', 'Links', 'Pieces Dropped', 'Status', 'Defense', 'Sabotage', 'Parked', 'Docked', 'Engaged', 'Notes']
        ]
        for entry in this.data:
            if entry['id'] == id:
                m_list.append([
                    # ''
                    entry['team'],
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