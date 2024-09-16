from datetime import datetime

name=input("enter your name: ")

lists='''
Rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 20/kg
oil     Rs 80/litre 
paneer  Rs 40/kg
boost   Rs 90/each
colgate Rs 40/each
'''     

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'Rice':20,'sugar':30,'salt':20,'oil':80,'paneer':40,'boost':90,'colgate':40}

option=int(input("for list of items press 1: "))
if option==1:
    print(lists)
for i in range (len(items)):
    inp1=int(input("if you want to buy press 1 or 2 to exit : "))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry the entered item is not avaiable") 
    else:
        print("you entered wrong number")
    inp=input("can i bil the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=", "Sourav supermarket", 25*"=")
            print(28*"=", "Hyderabad", 28*"=")
            print("Name: ",name,30*"=","Date: ",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,7*' ',6*' ',ilist[i],3*' ',qlist[i],9*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount: ','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount: ','Rs',finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting")
            print(75*"-")



                       


