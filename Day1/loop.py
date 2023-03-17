l = [1,2,3,4,5,16]
sum = 0

for i in l:
    sum = sum + i

print(sum)

if 1 in l:
    print("true")

for i in range(1,10):
    print(i)


x = 10

while(x>=0):
    print(x)
    x=x-2

x=100
while( x>=0):
    if(x%17) ==0:
        print(x)
        break
    else:
        x=x-1
        continue