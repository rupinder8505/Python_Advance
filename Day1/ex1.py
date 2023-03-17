a_list = [1,4,"a",0,"b",9]
sq_in = [e**2 
for e in a_list if "int" in str(type(e))]

print(sq_in)