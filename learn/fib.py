"""lim=int(input("enter the limit"))
n1=-1
n2=1
n=0
print("fibonacci series:")
for i in range (0,n):
     n = n1 + n2
     n1=n2
     n2=n
while n<=lim:
    if n%12==0:
      print(n)"""

lim=int(input("enter the limit"))
n1,n2=0,1
count=0
if lim<=0:
    print("sry")
else:
    print("series")
    while count<lim:
        if count%12==0:

            n=n1+n2
            n1=n2
            count+=1
            print(count)


