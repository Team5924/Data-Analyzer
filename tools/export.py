import pandas as pd
import numpy as np

def array(arr):
    data = np.delete(arr, 0, axis=1)
    data = pd.DataFrame(data)
    # 'index' should always be false; `header` should be list[] that labels each column
    data.to_csv("files/output.csv", index=False, header=False)