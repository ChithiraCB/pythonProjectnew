class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return (2*(self.length+self.breadth))
l1=int(input("Enter the length :"))
b1=int(input("Enter the breadth :"))
o1=rectangle(l1,b1)
x=o1.area()
y=o1.perimeter()
print("The area is :",x)
print("The perimeter is :",y)

l2=int(input("Enter the length:"))
b2=int(input("Enter the breadth :"))
o2=rectangle(l2,b2)
a=o2.area()
b=o2.perimeter()
print("The area is :",a)
print("The perimeter is :",b)

if(x>a):
    print("First rectangle is greater than second rectangle")
else:
    print("Second rectangle is greater than first rectangle")