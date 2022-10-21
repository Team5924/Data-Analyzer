import numpy as np
import pandas as pd

scouters = pd.read_csv("files/scouters.csv")
scouters = scouters.to_numpy()

# Removes the header from each entry
# "s=0" --> 0
# 'input' --> String

def entry(input, dtype):
    # Locates the index of the "="
    x = 0
    for i in input:
        if i == "=":
            x = x + 1
            break
        x = x+1
    m_entry = []
    # Extracts the data from 'input'; excludes the header
    for i in range(x, len(input)):
        m_entry.append(input[i])
    # 'dType' = True --> int; 'dType' = False --> string
    if not dtype:
        return "".join(m_entry)
    else:
        return int("".join(m_entry))

# Utilizes the 'entry()' to process and create a new array of data without the header

def array(arr):
    m_array = arr
    for m in range(len(arr)):
        for n in range(len(arr[m])):
            m_array[m][n] = int(entry(arr[m][n], True))
    return m_array

def names(arr):
    m_array = arr
    for m in range(len(arr)):
        for x in range(len(scouters)):
            if arr[m][1] == scouters[x][0]:
                m_array[m][1] = scouters[x][1]
    return m_array