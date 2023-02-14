n=int(input("Enter the limit:"))
n1=0
n2=1
n3=0
print("Fibonacci Series:")
'''print(n1)'''
if(n<=0):
    print("not possible")
else:
  for i in range(0, n):
    n1=n2
    n2=n3
    n3=n1+n2
    print(n3)

