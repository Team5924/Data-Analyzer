import numpy as np

# Makes a copy of 'arr' and replaces each row with only QT data

def qt(arr):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][0] == 0: # 'h=0' --> quantitative
            m_array[x] = arr[m]
            x = x + 1
    return m_array

# Makes a copy of 'arr' and replaces each row with only QL data

def ql(arr):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][0] == 1: # 'h=1' --> qualitative
            m_array[x] = arr[m]
            x = x + 1
    return m_array

# Makes a copy of 'arr' and replaces each row with only data from 'team'
# 'column' is the index of 'team' in 'arr'

def team(arr, team, column):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][column] == team:
            m_array[x] = arr[m]
            x = x + 1
    return m_array

# Makes a copy of 'arr' and replaces each row with only data from 'match'
# 'column' is the index of 'match' in 'arr'

def match(arr, match, column):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][column] == match:
            m_array[x] = arr[m]
            x = x + 1
    return m_array