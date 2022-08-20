import random
x=[]
a=int(input("The number of numbers in the list ? : "))
for i in range(a):
    b=random.randint(0,50)
    if b not in x:
        x.append(b)
print(x)