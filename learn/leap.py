"""n=int(input("enter the year"))
if(n%4==0):
   if(n%100==0):
       if(n%400==0):
           print("leap yr")
       else:
           print("not leap year")
   else:
       print(" leap yr")
else:
    print("not leap yr")
a=int(input("enter the lower limit year"))
b=int(input("enter the upper limit year"))
for i in range(a,b):
    if((i%400==0) or((i%100!=0) and (i%4==0))):
        print(i)

n=int(input("enter the limit"))
for i in range(0,n):
    sqr=i*i
    print(sqr)


n=int(input("enter no of elemnts"))
for i in range (0,n):
  num=int(input("enter integer"))
  if(num<100):
        print(num)
  else:
        print("over")

x=int(input("enter no"))
y=int(input("enter no"))
z=int(input("enter no"))
if((x>y) and (x>z)):
    print(x,"is grater")
elif((y>x)and(y>z)):
    print(y,"grater")
else:
    print(z,"is grater")

r=int(input("enter radius"))
a=3.14*r*r
print(a)


list=[-1,3,7,-9]
for i in list:
    if(i>0):
        print(i)

n=int(input("enter a number"))
if(n%2==0):
    print("even")
else:
    print("odd")

n = int(input("enter a no"))
for i in range(2, n):
    if (n % i == 0):
        print("not prime")
        break;
    else:
        print("prime")
        break;

ll=int(input("limit"))
ul=int(input("limit"))
for num in range (ll,ul+1):
    if num>1:
        for i in range(2,num):
          if(num%i)==0:
            break
        else:
            print(num)

lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)

n=int(input("enter limit"))
sqr=[i*i for i in range(0,n)]
print(sqr)

word=input("enter word")
for letter in word:
    if letter in "aeiou":
        print (letter)


list=["apple","mago"]
print(list)
print(len(list))
list.append("cherry")
print(list)
list.insert(1 ,"berry")
print(list)
list.pop(2)
print(list)
print(list[-1:])
list.reverse()
print(list)


str=input("enter a string")
#for i in str:
a=str[0]
b=str[1:-1]
c=str[-1]
print(c+b+a)

file=input("enter filename")
ex=file.split(".")
print(ex[1])


str=input("enter a string")
a=str[0]
for i in str:
    if(i==a):
        str=str.replace(i,"$")
        str=a+str[1:]
print(str)

lim=int(input("enter the no of elemnts"))
print(" the integers")
list=[]
for i in range(0,lim):
  ele=int(input()t("enter integeers")
  if (ele>100):
    list.append("over")
  else:
    list.append(ele)
print(list)
lim=int(input("enter limit"))

list=[]
print("enter elements")
for i in range(0,lim):
  n=int(input())
  if(n%2!=0):
    list.append(n)
print(list)

d = {1: 0, 3: 9, 2: 1}
sortd = sorted(d.items())
print(sortd)
sortdd=sorted(d.items(),reverse=True)
print(sortdd)

n=int(input("enter the limit"))
n1=-1
n2=1
print("fib:")
for i in range(0,n):
   n = n1 + n2
   print(n)
   n1=n2
   n2=n

n=int(input("eneter a no"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

n=int(input("enter no of strings"))
print("strings")
count=0
list=[]
for i in range(0,n):
    str=input()
    list.append(str)
print(list)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1
print(count)

str=input("enter a string")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for m,n in dict.items():
    print(m,n)

str=input("enter a text")
word=str.split(" ")
print(word)
dict={}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for m,n in dict.items():
    print(m,n)

m=int(input("enter no of colour"))
list1=[]
for i in range(0,m):
    clr=input()
    list1.append(clr)
print(list1)
n=int(input("eneter no of colour"))
list2=[]
for i in range(0,n):
    clr2=input()
    list2.append(clr2)
print(list2)
clrlist=list(set(list1).difference(list2))
print(clrlist)

str=input("str")
if (str[-3:]=="ing"):
    str=str.replace(str[-3:],"ly")
else:
    str=str+"ing"
print(str)"""

def factor(n):

    for i in range(1,n+1):
        if(n%i==0):
            print(i)
n = int(input("enter a number"))
factor(n);



