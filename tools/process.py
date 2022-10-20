import numpy as np

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
    m_array = np.zeros(np.shape(arr), np.int8)
    for m in range(len(arr)):
        for n in range(len(arr[m])):
            m_array[m][n] = entry(arr[m][n], True)
    return m_array