class firstnumber:
    def __int__(self, a):
        self.a = a  # int(input("enter the element to class A :"))


class secondnumber(firstnumber):
    def __int__(self, b, a):
        self.b = b  # int(input("enter the element to class B :"))
        firstnumber.__int__(self, a)


class thirdnumber(secondnumber):
    def __int__(self, c, b, a):
        self.c = c  # int(input("enter the element to class C :"))
        secondnumber.__int__(self, b, a)

a = thirdnumber()
if a.a > a.b and a.b > a.c:
    print("element of class A is greatest :", a.a)
elif a.b > a.a and a.a > a.c:
    print("element of class A is greatest :", a.b)
else:
    print("element of class A is greatest :", a.c)
