import pandas as pd

def array(arr):
    data = pd.DataFrame(arr)
    # 'index' should always be false; `header` should be list[] that labels each column
    data.to_csv("files/output.csv", header=True)