m=int(input("Enter no of colours in 1st list:"))
print("enter the colours");
colour_list1=[]
for i in range(0,m):
    i=input()
    colour_list1.append(i)
#print(colour_list1)
n=int(input("Enter no of colours in 2nd list:"))
print("enter the colours")
colour_list2=[]
for i in range(0,n):
    i=input()
    colour_list2.append(i)
#print(colour_list2)
print("colour present in list1 but not in list2 are:")
c=list(set(colour_list1).difference(colour_list2))
print(c)

