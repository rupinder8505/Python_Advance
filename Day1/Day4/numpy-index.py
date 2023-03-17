import numpy as np

a = np.array([1,2,3,4,7,8,6])

#print(a[2])

b = np.arange(15).reshape(3,5)

#print(b[0,2])  #fast

#print(b[0][2]) #slow

print(a[2:7:2])
print(b)

print(b[1:3,1:3])