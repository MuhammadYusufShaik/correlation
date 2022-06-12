
import pandas as pd
import numpy as np
df =pd.read_csv('C:/Users/khada/Downloads/python/c106/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv')
temperature=df['Temperature'].tolist()
icecream=df['Ice-cream Sales( ₹ )'].tolist()
d={'x':temperature,'y':icecream}
correlation=np.corrcoef(d['x'],d['y'])
print(correlation)