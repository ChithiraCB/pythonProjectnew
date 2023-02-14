class first():
    def __init__(self):
        self.a=int(input("enter the element :"))


class second(first):
    def __init__(self):
        first.__init__(self)
        self.b= int(input("enter the element :"))


class third(second):
    def __init__(self):
        second.__init__(self)
        self.c = int(input("enter the element :"))

a=third()
if a.a > a.b and a.b > a.c:
    print("element of class first is greatest ",a.a)
elif a.b > a.a and a.a > a.c:
    print("element of class second is greatest ", a.b)
else:
    print("element of class third is greatest ", a.c)



