n=int(input("enter number of elements"))
print("enter elements")
list=[]
for i in range(0,n):
    element=int(input())
    if(element%2!=0):
        list.append(element)
print(list)


