import numpy as np
import pandas as pd
from packages.Analyzer.modules import process
pd.set_option('display.max_columns', 100)

class Pit:
    def __init__(this, data) -> None:
        this.data = data

    # Displays the pit data for all teams
    def display(this) -> pd.DataFrame:
        m_list = []
        labels = [
            'iD',
            'Team',
            'Speed (ft/sec)',
            'Drivetrain',
            'Auto',
            'Climb Time',
            'Substation',
            'Pickup',
            'Pieces',
        ]
        for entry in this.data:
            m_list.append([
                process.id(entry['id']),
                entry['team'],
                entry['speed'],
                entry['drivetrain'],
                entry['auto'],
                entry['climbTime'],
                entry['substation'],
                entry['pickup'],
                entry['pieces'],
            ])
        
        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df
    
    # Looks up a specific team's pit data
    def lookup(this, team: int) -> pd.DataFrame:
        m_list = []
        labels = [
            'iD',
            'Team',
            'Speed (ft/sec)',
            'Drivetrain',
            'Auto',
            'Climb Time',
            'Substation',
            'Pickup',
            'Pieces',
        ]
        for entry in this.data:
            if entry['team'] == team:
                m_list.append([
                process.id(entry['id']),
                entry['team'],
                entry['speed'],
                entry['drivetrain'],
                entry['auto'],
                entry['climbTime'],
                entry['substation'],
                entry['pickup'],
                entry['pieces'],
            ])
        
        df = pd.DataFrame(m_list, columns=labels)
        df.index += 1
        return df