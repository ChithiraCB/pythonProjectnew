class rectangle():
    def __init__(self):
        self._length = int(input("Enter the Length:"))
        self._breadth = int(input("Enter the Breadth:"))
        self.area = self._length * self._breadth
    def greaterThan(self,rectangle):
        if self.area < rectangle.area:
            print("First rectangle is Greater")
        else:
            print("Second rectangle is Greater")
r1=rectangle()
print("area of first rectangle:",r1.area)
r2=rectangle()
print("area of second rectangle:",r2.area)
r2.greaterThan(r1)