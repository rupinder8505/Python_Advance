import numpy as np

a = np.array([1,3,5,-1,-5,4,10])

print(a[a<0])

print(a[np.all([a<0,a%2!=0],axis=0)])

