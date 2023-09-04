import random
x=[]
a=int(input("The number of list members ? : "))
while True:
    if len(x)==a:
        break
    else:
        b=random.randint(0,50)
        if b not in x:
            x.append(b)
print(x)
