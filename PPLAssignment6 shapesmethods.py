import math
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am 2 dimensional shape"
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def area(self):
        print( "Area of square is" ,self.length**2)
    def fact(self):
        return "Square have each angle equal to 90"
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        print( " Area of circle is", pi*self.radius**2)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
        print("Triangle")
    def area(self):
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        print("Area of triangle is", area)
class Quadrilateral(Shape):
    def __init__(self, q, r, s, t):
        self.side1=q
        self.side2=r
        self.side3=s
        self.side4=t
    def Perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("Perimeter = ", p)
class Rectangle(Quadrilateral):
    def __init__(self, a, b):
        print("Rectangle")
        super().__init__(a, b, a, b)


        
a = Square(4)
print(a)
print(a.fact())
print(a.area())
b = Circle(7)
print(b)
print(b.fact())
print(b.area())
c = Quadrilateral(7,5,6,4)
c.Perimeter()
d = Rectangle(10, 20)
d.Perimeter()
e = Triangle(3,4,5)
e.area()

