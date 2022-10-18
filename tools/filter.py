import numpy as np

def qt(arr):
    array = np.empty(np.shape(arr), np.int8)
    x = 0
    for m in range(len(arr)):
        if arr[m][0] == 0:
            array[x] = arr[m]
            x = x + 1
        else:
            array[x] = np.zeroes(np.shape(array), np.int8)
            x = x + 1
    return array
