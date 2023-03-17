import numpy as np

print(np.__version__)

a = np.array([1,3,5,6],dtype=np.float64)
#print(a)
#print(a.dtype)

x = np.array([[1,2,3],[5,6,7]])
#print(x)
#print(x[1:3,1:3])
t = np.arange(15).reshape(3,5)
print(t)
print(t.shape) ##(3,5)

z=np.arange(10,30,5).reshape(2,2)
print(z)

c = np.linspace(0,1,10)

print("enter min")
min=input()
print("enter max")
max=input()
#if(max<min):
#print("not valid entry")
#else:
print("Enter number of numbers")
num = input()
k = np.linspace(int(min),int(max),int(num))

print(k)
