import pickle
class Laptop:
    def __init__(self,name,price):
        self.name = name
        self.price= price

    def details(self):
        print("Name"+self.name)
f = open("pk.txt","rb")

dct = pickle.load(f)
print(dct.details())
f.close()