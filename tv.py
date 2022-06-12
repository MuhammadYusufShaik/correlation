import pandas as pd
import numpy as np
df =pd.read_csv('C:/Users/khada/Downloads/python/c106/Student Marks vs Days Present.csv')
marks=df['Marks In Percentage'].tolist()
day=df['Days Present'].tolist()
d={'x':day,'y':marks}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)