people = [(2,"Sara"),(1,"Bob"),(3,"Mary")]
people.sort(key=lambda x : x[1])
print(people)

a = [1,2,3,4,5]
b=[1,2,3,4,5]
sq = list(map (lambda x,y:x*y,a,b))
print(sq)

seq = ['a','e','i','o','u','f','t']

def vowel_check(x):
    vow=['a','e','i','o','u']
    if x in vow:
        return True
    else :
        return False

final_list = list(filter(vowel_check,seq))
print(final_list)

'''reduce'''

from functools import reduce
numbers = [47,15,25,55,102]
maxNumber = reduce( lambda x,y: x if x>y else y, numbers) 
print(maxNumber)