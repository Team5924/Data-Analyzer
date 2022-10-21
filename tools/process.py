import numpy as np
import pandas as pd

scouters = pd.read_csv("files/scouters.csv")
scouters = scouters.to_numpy()

# Process all entries at once; all process functions here

def all(arr):
    m_array = arr
    m_array = array(m_array)
    m_array = names(arr, 1)
    m_array = alliance(arr, 3)
    m_array = as_pos(arr, 5)
    m_array = taxi(arr, 6)
    m_array = climb(arr, 13)
    return m_array

# Removes the header from each entry
# "s=0" --> 0
# 'input' = string

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

def names(arr, index):
    m_array = arr
    for m in range(len(arr)):
        for i in range(len(scouters)):
            if arr[m][index] == scouters[i][0]:
                m_array[m][index] = scouters[i][1]
    return m_array

def alliance(arr, index):
    m_array = arr
    for m in range(len(arr)):
        if arr[m][index] % 2 == 0:
            m_array[m][index] = "Red"
        else:
            m_array[m][index] = "Blue"
    return m_array

# Simple function for processing only data that is binary

def binary(arr, index):
    m_array = arr
    for m in range(len(arr)):
        if arr[m][index] == 0:
            m_array[m][index] = "No"
        if arr[m][index] == 1:
            m_array[m][index] = "Yes"
    return m_array