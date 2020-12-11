class Animal(object):
    def __init__(self):
        print("This is an animal")
    def eat(self):
        print("I can eat")
    def run(self):
        print("I can run")
class Dog(Animal):
    def __init__(self):
        print("I am dog")
    def bark(self):
        print("Dog can bark")
class Snake(Animal):
    def __init__(self):
        print("I am snake")
    def sound(self):
        print("Snake makes a hiss sound ")
    def body(self):
        print("Snake's body is covered with scales")
    def move(self):
        print("Snakes slithers")
class Horse(Animal):
    def __init__(self):
        print("I am horse")
    def sound(self):
        print("Horse neighs!")
    def move(self):
        print("Horse shows galloping")
    def body(self):
        print("Horse has hooves and tails")
class Bird(Animal):
    def __init__(self):
        print("I am bird")
    def fly(self):
        print("Bird flies in the sky")
    def sing(self):
        print("Bird sings sweetly")
    def place(self):
        print("Birds live in nests")
class Turtle(Animal):
    def __init__(self):
        print("I am turtle")
    def run(self):
        print("Turtles can't run fast")
    def home(self):
        print("Turtles lives in shell")
class Fish(Animal):
    def __init__(self):
        print("I am fish")
    def swim(self):
        print("Fishes can swim")
    def body(self):
        print("Fishes has gills on the body")
    def place(self):
        print("Fishes lives in water")

    
 
d1 = Dog()
d1.eat()
d1.run()
d1.bark()
s1 = Snake()
s1.eat()
s1.sound()
s1.move()
s1.body()
h1 = Horse()
h1.eat()
h1.sound()
h1.move()
h1.body()
b1 = Bird()
b1.eat()
b1.fly()
b1.sing()
b1.place()
t1 = Turtle()
t1.eat()
t1.home()
f1 = Fish()
f1.swim()
f1.eat()
f1.body()
f1.place()
    