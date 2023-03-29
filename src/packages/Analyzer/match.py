import numpy as np
import pandas as pd
from packages.Analyzer.modules import process, calculate
pd.set_option('display.max_columns', 100)

class Match:
    def __init__(this, data) -> None:
        this.data = data

    # Returns the raw data as a pandas DataFrame; really only useful for debugging
    def display(this):
        df = pd.DataFrame(this.data)
        return df
    
    def blue_alliance(this, match):
        blue = []
        labels = [
            ['Metadata'] * 3 + ['Auto'] * 3 + ['Score (Auto)'] * 3 + ['Score (Teleop)'] * 3 + ['Teleop'] * 5 + ['Endgame'] * 3 + ['Misc'],
            ['iD', 'Team', 'Attendance', 'Mobility', 'Docked', 'Engaged', 'Top', 'Mid', 'Bot', 'Top', 'Mid', 'Bot', 'Links', 'Pieces Dropped', 'Status', 'Defense', 'Sabotage', 'Parked', 'Docked', 'Engaged', 'Notes']
        ]
        for entry in this.data:
            if entry['match'] == match:
                if entry['alliance'] <= 2:
                    blue.append([
                        # ''
                        process.id(entry['id']),
                        entry['team'],
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
        
        df = pd.DataFrame(blue, columns=labels)
        df.index += 1
        return df
    
    def red_alliance(this, match):
        red = []
        labels = [
            ['Metadata'] * 3 + ['Auto'] * 3 + ['Score (Auto)'] * 3 + ['Score (Teleop)'] * 3 + ['Teleop'] * 5 + ['Endgame'] * 3 + ['Misc'],
            ['iD', 'Team', 'Attendance', 'Mobility', 'Docked', 'Engaged', 'Top', 'Mid', 'Bot', 'Top', 'Mid', 'Bot', 'Links', 'Pieces Dropped', 'Status', 'Defense', 'Sabotage', 'Parked', 'Docked', 'Engaged', 'Notes']
        ]
        for entry in this.data:
            if entry['match'] == match:
                if entry['alliance'] > 2:
                    red.append([
                        # ''
                        process.id(entry['id']),
                        entry['team'],
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
        
        df = pd.DataFrame(red, columns=labels)
        df.index += 1
        return df
    
    # Returns the data for a specific match
    def num(this, match: int) -> pd.DataFrame:
        m_list = []
        for entry in this.data:
            if entry['match'] == match:
                m_list.append(entry)

        df = pd.DataFrame(m_list)
        return df