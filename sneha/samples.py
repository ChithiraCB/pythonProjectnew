"""f=open("demo.txt","r")
list=f.readlines()
print(list)
f.close()

f1=open("demo.txt","r")
f2=open("newodd.txt","w")
a=f1.readlines()
for i in range(0,len(a)):
    if (i%2!=0):
        f2.write(a[i])
    else:
        pass
f1.close()
f2.close()
f=open("newodd.txt","r")
b=f.readlines()
print("odd lines are :",b)
f.close()

f = open('odd.txt','r')
print(f.closed)
f.close()
print(f.closed)

import csv
c_col=['id','name','age']
dict_data=[{'id':1,'name':'g','age':20}]
try:
    with open("name.csv","w") as f :
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
           write.writerow(i)
except IOError:
    print("input output error")
d=csv.DictReader(open("name.csv"))
print("output is")
for i in d:
    print(i)"""
from sneha.ex36 import bank


class bank:
    def __init__(self,acn,name,accty):
        self.acn=acn
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("acctno:",self.acn)
        print("name:", self.name)
        print("accty:", self.accty)
        print("balance=",self.bal)
    def deposit(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal
    n=input("name")
    a=int(input("accno"))
    t=input("type")
    o= bank(a,n,t)
    o.showamount()
    while(True):
        print("1.deposit")
        print("2.withdraw")
        c=int(input("enter your choice "))
        if(c==1):
            d=int(input("eneter amt to depo"))
            print("ttl balna",o.deposit(d))
        elif(c==2):
            w=int(input("withdraw"))
            if(w>d):
                print("insuf bal")
            else:
                print("balnce",o.withdraw(d))
        else:
            print("invalid")












