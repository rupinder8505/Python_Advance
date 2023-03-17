import pandas as pd

s = pd.DataFrame({'x':[1,4],'y':[2,5],'z':[6,7]})

print(s)

data = {'Name':['Tom','Jack',"Steve"],'Age':[28,30,40]}

j = pd.DataFrame(data,index=['first','second','third'])

print(j)