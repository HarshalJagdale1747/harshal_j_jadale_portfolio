import numpy as np
import pandas as pd
data=np.loadtxt('data.csv',delimiter=',',dtype=str)
data1=pd.read_csv('data.csv')
print(data)
print(data1)
