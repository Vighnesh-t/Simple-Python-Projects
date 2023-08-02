prod=[]
price=[]
bill=0
b1=str(input("enter product:"))
prod.append(b1)
while True:
    a=str(input("y for add more food and N for close :"))
    if(a=="y"):
        b2=str(input("enter product:"))
        prod.append(b2)
    elif(a=="n"):
        break
print("-----------------------------------")
for c in range(0,len(prod)):
    print("Enter ",prod[c],"price:")
    d=int(input())
    price.append(d)
print("-----------------------------------")
f=str(input("If you want to enter GST press y else press n for Bill: "))
if(f=="y"):
    print("------------JOY FOOD STORE--------------")
    GST=int(input("enter GST:"))
    print("** YOUR BILL **")
    for g in range(0,len(price)):
        bill=bill+price[g]
        print(prod[g],":",price[g])
    print("---------------------------------")
    total=(bill*GST)/100
    print("Total Bill(GST INCLUDED):",total+bill)
elif(f=="n"):
    print("------------JOY FOOD STORE--------------")
    print("** YOUR BILL **")
    for g in range(0,len(price)):
        print(prod[g],":",price[g])
        bill=bill+price[g]
    print("---------------------------------")
    print("Total Bill(GST NOT INCLLUDED):",bill)