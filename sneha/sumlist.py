n=int(input("enter number of elements in the list :"))
list=[]
print("enter elements")
for i in range (0,n):
    x=int(input())
    list.append(x)
s=sum(list)
print("sum of all elements in the list is",s)