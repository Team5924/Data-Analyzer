import numpy as np

def json_to_array(array):
    m_array = []
    for entry in range(len(array)):
        m_entry = []
        m_dict = array[entry]
        for key in array[entry]:
            m_entry.append(m_dict[key])  
        m_array.append(m_entry)

    return np.array(m_array)  