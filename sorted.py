a=[]
b=int(input("The number of numbers in the list ? : "))
for i in range(b):
    c=int(input("Your list numbers : "))
    a.append(c)
if sorted(a)==a:
    print("True")
else:
    print("wrong")
