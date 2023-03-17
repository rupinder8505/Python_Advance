import pickle

class Laptop:
    def __init__(self,name,price):
        self.name = name
        self.price= price

    def details(self):
        print("Name"+self.name)

Laptop1 = Laptop('Asus',2000)
'''
dict = {"name":"John","family":"Doe","age":20}

f=open("pk.txt","wb")
pickle.dump(dict,f)
'''
f=open("pk.txt","wb")
pickle.dump(Laptop1,f)

f.close()