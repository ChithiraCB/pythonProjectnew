class bank:
    def __init__(self,accn,name,accty):
        self.accn=accn
        self.name=name
        self.accty=accty
        self.bal=0
    def showamount(self):
        print("The account no is :",self.accn)
        print("account holder name :",self.name)
        print("account type :",self.accty)
        print("balance :",self.bal)

    def deposit(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withdraw(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("enter your name :")
a=int(input("enter your account number :"))
t=input("enter account type :")
o=bank(a,n,t)
o.showamount()
while(True):
    print("MENU")
    print("\n1.Deposit")
    print("\n2.withdraw")
    c=int(input("enter your choice :"))
    if(c==1):
        d=int(input("enter the amount to deposit :"))
        print("your total balance amount is:",o.deposit(d))


    elif(c==2):
        w=int(input("enter the amount to withdraw :"))
        if(w>d):
            print("Insufficient balance ")
        else:
            print("your total balance amount is :",o.withdraw(w))
    else:
        print("Enter valid choice")