import numpy as np
import pandas as pd
import math
from files.id import id_list

class Data:
    def __init__(self, value) -> None:
        self.value = value

    ### * ------- ###
    ### * GENERAL ###
    ### * ------- ###

    # ? Displays the data as a pandas Dataframe
    def display(self):
        df = pd.DataFrame(self.value)
        df['Team'] = df['Team'].astype('Int64')
        return df
    
    # ? Filters between quantitative, qualitative, and pit data
    # * @param {str} type
    def filter(self, type):
        m_list = []
        for entry in self.value:
            if entry['Type'] == type:
                m_list.append(entry)

        for entry in m_list:
            entry.pop('Type')

        self.value = m_list
        return self

    # ? Filters out data on a specific team 
    # * @param {str} team
    def team(self, team):
        m_list = []
        for entry in self.value:
            if entry['Team'] == team:
                m_list.append(entry)

        self.value = m_list
        return self

    # ? Filter out a specific match
    # * @param {int} match
    def match(self, match):
        m_list = []; blue = []; red = [];
        for entry in self.value:
            if entry['Match'] == match:
                if entry['Alliance'] <= 2:
                    blue.append(entry)
                if entry['Alliance'] > 2:
                    red.append(entry)

        m_list.extend(blue)
        m_list.extend(red)

        self.value = m_list
        return self
    
    def id(self, id):
        m_list = []
        for entry in self.value:
            if entry['iD'] == id:
                m_list.append(entry)

        self.value = m_list
        return self
    
    # ? Calculates the average occurence of a certain field
    def calc_avg(self, team, field, occurence):
        matches = 0
        counter = 0
        for entry in self.value:
             if entry['Team'] == team:
                matches += 1
                if entry[field] == occurence:
                    counter += 1

        try:
            avg = round(counter / matches, 4) * 100
        except:
            avg = None
        return avg
    
    # ? Sorts data by a field, in descending order
    # * @param {string} field
    def sort(self, field):
        df = pd.DataFrame(self.value)
        df.sort_values(field, ascending=False)
        return pd.DataFrame(self.value).sort_values(field, ascending=False)
    
    ### * --------------- ###
    ### * SEASON SPECIFIC ###
    ### * --------------- ###

    # ? Generates the teleop grid
    #   Formula = total grid - auto grid
    # * @param{int} team
    def generate_teleopGrid(self):
        for entry in self.value:
            autoTop = np.array(entry['Score (Auto)']['top'])
            totalTop = np.array(entry['Score (Total)']['top'])
            teleopTop = (totalTop - autoTop).tolist()
            for i, node in enumerate(teleopTop):
                if node == -1:
                    teleopTop[i] = 0

            autoMid = np.array(entry['Score (Auto)']['mid'])
            totalMid = np.array(entry['Score (Total)']['mid'])
            teleopMid = (totalMid - autoMid).tolist()

            autoBotCone = np.array(entry['Score (Auto)']['botCone'])
            totalBotCone = np.array(entry['Score (Total)']['botCone'])
            teleopBotCone = (totalBotCone - autoBotCone).tolist()

            autoBotCube = np.array(entry['Score (Auto)']['botCube'])
            totalBotCube = np.array(entry['Score (Total)']['botCube'])
            teleopBotCube = (totalBotCube - autoBotCube).tolist()

            teleopGrid = {
                'top': teleopTop,
                'mid': teleopMid,
                'botCone': teleopBotCone,
                'botCube': teleopBotCube
            }

            entry.update({'Score (Teleop)': teleopGrid})

        return self
    
    # ? Process fields
    def process(self):
        for entry in self.value:
            for id in id_list:
                if id[0] == entry['iD']:
                    entry['iD'] = id[1]

            match entry['Alliance']:
                case 0:
                    entry['Alliance'] = 'Blue-1'
                case 1:
                    entry['Alliance'] = 'Blue-2'
                case 2:
                    entry['Alliance'] = 'Blue-3'
                case 3:
                    entry['Alliance'] = 'Red-1'
                case 4:
                    entry['Alliance'] = 'Red-2'
                case 5:
                    entry['Alliance'] = 'Red-3'

            match entry['No Show']:
                case 0:
                    entry['No Show'] = 'No'
                case 1:
                    entry['No Show'] = 'Yes'

            match entry['Mobility']:
                case 0:
                    entry['Mobility'] = 'No'
                case 1:
                    entry['Mobility'] = 'Yes'

            match entry['Docked (Auto)']:
                case 0:
                    entry['Docked (Auto)'] = 'No'
                case 1:
                    entry['Docked (Auto)'] = 'Yes'

            match entry['Engaged (Auto)']:
                case 0:
                    entry['Engaged (Auto)'] = 'No'
                case 1:
                    entry['Engaged (Auto)'] = 'Yes'   
            
            match entry['Disabled']:
                case 0:
                    entry['Disabled'] = 'No'
                case 1:
                    entry['Disabled'] = 'Yes'

            match entry['Parked']:
                case 0:
                    entry['Parked'] = 'No'
                case 1:
                    entry['Parked'] = 'Yes'

            match entry['Docked (Endgame)']:
                case 0:
                    entry['Docked (Endgame)'] = 'No'
                case 1:
                    entry['Docked (Endgame)'] = 'Yes'

            match entry['Engaged (Endgame)']:
                case 0:
                    entry['Engaged (Endgame)'] = 'No'
                case 1:
                    entry['Engaged (Endgame)'] = 'Yes'

            auto = {
                'top': sum(entry['Score (Auto)']['top']),
                'mid': sum(entry['Score (Auto)']['mid']),
                'botCone': sum(entry['Score (Auto)']['botCone']),
                'botCube': sum(entry['Score (Auto)']['botCube'])
            }

            teleop = {
                'top': sum(entry['Score (Teleop)']['top']),
                'mid': sum(entry['Score (Teleop)']['mid']),
                'botCone': sum(entry['Score (Teleop)']['botCone']),
                'botCube': sum(entry['Score (Teleop)']['botCube'])
            }

            total = {
                'top': sum(entry['Score (Total)']['top']),
                'mid': sum(entry['Score (Total)']['mid']),
                'botCone': sum(entry['Score (Total)']['botCone']),
                'botCube': sum(entry['Score (Total)']['botCube'])
            }

            # Popping and then replacing; more orderly
            entry.pop('Score (Auto)')
            entry.pop('Score (Teleop)')
            entry.pop('Score (Total)')

            entry.update({'Score (Auto)': auto})
            entry.update({'Score (Teleop)': teleop})
            entry.update({'Score (Total)': total})

        return self

    # ? Calculates the average point for auto
    # * @param {int} team
    def calc_avg_autoPointsScored(self, team):
        top = 0; mid = 0; botCone = 0; botCube = 0; bot = 0; total = 0; matches = 0
        for entry in self.value:
            if entry['Team'] == team:
                matches += 1

                top += sum(entry['Score (Auto)']['top']) * 6
                mid += sum(entry['Score (Auto)']['mid']) * 4
                botCone += sum(entry['Score (Auto)']['botCone'])
                botCube += sum(entry['Score (Auto)']['botCube'])
                bot = (botCone + botCube) * 3

        total = top + mid + bot
        avg_points = round(total / matches, 2)
        return avg_points
    
    # ? Calculate the average point for teleop
    # * @param {int} team
    def calc_avg_teleopPointsScored(self, team):
        top = 0; mid = 0; botCone = 0; botCube = 0; bot = 0; total = 0; matches = 0
        for entry in self.value:
            if entry['Team'] == team:
                matches += 1

                top += sum(entry['Score (Teleop)']['top']) * 5
                mid += sum(entry['Score (Teleop)']['mid']) * 3
                botCone += sum(entry['Score (Teleop)']['botCone'])
                botCube += sum(entry['Score (Teleop)']['botCube'])
                bot = (botCone + botCube) * 2

        total = top + mid + bot
        avg_points = round(total / matches, 2)
        return avg_points
    
    # ? Compares a list of teams
    # * @param {list} teams
    def compare_teams(self, teams):
        m_list = []
        for team in teams:
            m_list.append({
                'Team': team,
                'Mobility %': self.calc_avg(team, 'Mobility', 1),
                'Avg Docked (Auto) %': self.calc_avg(team, 'Docked (Auto)', 1),
                'Engaged (Auto) %': self.calc_avg(team, 'Docked (Auto)', 1),
                'Avg Auto Points Scored': self.calc_avg_autoPointsScored(team),
                'Avg Teleop Points Scored': self.calc_avg_teleopPointsScored(team),
                'Docked (Endgame) %': self.calc_avg(team, 'Docked (Endgame)', 1),
                'Endgame (Endgame) %': self.calc_avg(team, 'Docked (Endgame)', 1)
            })
        
        self.value = m_list
        return self
    
    # ? Display the alliance grids & links from a specific match
    def alliance_grids(self):
        # * try and excepts are used because sometimes not all 6 robots are scouted per match
        # Create grids
        blue = np.zeros((3, 9), dtype=np.int64)
        red = np.zeros((3, 9), dtype=np.int64)
        for entry in self.value:
            top = np.array(entry['Score (Total)']['top'])
            mid = np.array(entry['Score (Total)']['mid'])
            botCone = np.array(entry['Score (Total)']['botCone'])
            botCube = np.array(entry['Score (Total)']['botCube'])
            bot = botCone + botCube

            # Separate data by alliance
            if entry['Alliance'] <= 2:
                blue += [top, mid, bot]
            if entry['Alliance'] > 2:
                red += [top, mid, bot]

        try:
            for row in blue:
                for i in range(len(row)):
                    if row[i] > 1:
                        row[i] = 1
            for row in red:
                for i in range(len(row)):
                    if row[i] > 1:
                        row[i] = 1
        except:
            pass

        # Counting links
        blue_links = 0
        red_links = 0
        count = 0
        try:
            for row in blue:
                for i in range(len(row)):
                    match row[i]:
                        case 1:
                            count += 1
                        case 0:
                            blue_links += math.floor(count / 3) # Original Concept by Wilson Chen
                            count = 0
                blue_links += math.floor(count / 3)
                count = 0
        except:
            pass
        try:
            for row in red:
                for i in range(len(row)):
                    match row[i]:
                        case 1:
                            count += 1
                        case 0:
                            red_links += math.floor(count / 3) # Original Concept by Wilson Chen
                            count = 0
                red_links += math.floor(count / 3)
                count = 0
        except:
            pass
        
        print('Blue Alliance,', 'Links:', blue_links)
        try:
            print(blue)
        except:
            pass
        print('\n')
        print('Red Alliance,', 'Links:', red_links)
        try:
            print(red)
        except:
            pass

        return self