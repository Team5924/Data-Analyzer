import numpy as np

# Makes a copy of "arr" and replaces each row with only QT data

def qt(arr):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][0] == 0: # "h=0" --> quantitative
            m_array[x] = arr[m]
            x = x + 1
    return m_array

# Makes a copy of "arr" and replaces each row with only QL data

def ql(arr):
    m_array = np.zeros(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][0] == 1: # "h=1" --> qualitative
            m_array[x] = arr[m]
            x = x + 1
    return m_array