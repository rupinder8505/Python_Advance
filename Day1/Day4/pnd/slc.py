import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,5,np.nan])

print(s)

data = np.array(["a","b","c"])

s= pd.Series(data)

print(s)

j = pd.Series(5,index=["a","b","c",1],dtype=np.complex128)

print(j)

d= pd.Series({'Jan':1,'Feb':2,'Mar':3,'Jan':5})
print(d['Jan'])