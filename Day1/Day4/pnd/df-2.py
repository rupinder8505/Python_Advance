import  pandas as pd

cities = pd.DataFrame({
    'city':["SF","Seattle","LA"],
    'pop':[10,20,30],
    'rain':[1,3,5]
})

print(cities.dtypes)

lv_df = pd.DataFrame({'city':["LV"],'pop':[24],'rain':[21]})

cities = pd.concat([cities,lv_df])

print(cities)


a=cities.iloc[[0]]

print(a)

print(cities["pop"])

print(cities.iloc[:,0:2])
cities["area"]=pd.Series([231,576,987,675])
print(cities)

a = cities.pop('rain')
print(cities)
print(a)

cities = cities.reset_index(drop=True)
print(cities)

cities.reset_index(drop=True,inplace=True)  # inmemory place optimization
print(cities)

cities=cities.drop(3)
print(cities)

c= cities.iloc[1:2,[0,1,2]]
print(c)

c2 = cities.set_index("city")
print(c2)

print(c2.loc["Seattle","LA"])

