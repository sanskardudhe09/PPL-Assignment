import turtle
s = turtle.getscreen()
t = turtle.Turtle()
class Shape:
    def __init__(self, sides = 0, length = 0):
        self.sides = sides
        self.length = length
class Polygon(Shape):
    def information(self):
        print("In geometry, a polygon is a plane figure that is described by finite number of straight line segments")
class Square(Polygon):
    def display(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
class Triangle(Polygon):
    def display(self):
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
class Pentagon(Polygon):
    def display(self):
        for i in range(4):
            t.forward(self.length)
            t.right(90)
class Hexagon(Polygon):
    def display(self):
        for i in range(6):
            t.forward(self.length)
            t.right(60)
class Octagon(Polygon):
    def display(self):
        for i in range(8):
            t.forward(self.length)
            t.right(45)
hex1 = Hexagon(6,100)
hex1.information()
hex1.display()
tri1 = Triangle()
tri1.information()

tri1.display()
pen1 = Pentagon()
pen1.information()
pen1.display()
oct1 = Octagon()
oct1.information()
oct1.display()


