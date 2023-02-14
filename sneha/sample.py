"""class myclass:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def show(self):
        print(self.fname,self.lname)
x=myclass("hi","bye")
x.show()

class Publisher():
    def __init__(self,pubname):
        self.pubname =pubname
    def display(self):
        print("Publisher :", self.pubname)

class Book(Publisher):
    def __init__(self,pubname):
        Publisher.__init__(self,pubname)

    def bookdetails(self):
        self.title= input("Book Name :")
        self.author = input("Book Author :")

    def display(self):
        print("Title :", self.title)
        print("Authur :", self.author)

class Python(Book):
    def __init__(self,pubname):
        Book.__init__(self,pubname)
    def moredetails(self):
        self._price = int(input("Book Price :"))
        self._pages = int(input("Book Pages :"))
    def display(self):
        print("Publisher :",self.pubname)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self._price)
        print("Pages :",self._pages)

obj = Python("abc books")
obj.bookdetails()
obj.moredetails()
print("___________________________________________")
obj.display()

class time():
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def add(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=time(2,10,5)
o2=time(4,5,10)
print(o2.add(o1))"""


class rectangle():
    def __init__(self):
        self._length = int(input("Enter the Length:"))
        self._breadth = int(input("Enter the Breadth:"))
        self.area = self._length * self._breadth
    def greaterThan(self,rectangle):
        if self.area < rectangle.area:
            print("1 is Greater")
        else:
            print("2 is Greater")
r1=rectangle()
print("1:",r1.area)
r2=rectangle()
print("2:",r2.area)
r2.greaterThan(r1)