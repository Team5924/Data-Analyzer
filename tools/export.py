import pandas as pd
import numpy as np

# 'labels' should be a list[]
# set 'labels' = False for no headers

def array(arr, labels):
    data = pd.DataFrame(arr, columns=labels)
    data.to_csv("files/output.csv", index=False, header=labels)