class Aquatic:
    def __init__(self):
        print("I am aquatic animal")
    def place(self):
        print("I lives in water")
class Shark(Aquatic):
    def __init__(self):
        print("I am shark")
    def swim(self):
        print("Shark swims")
    def body(self):
        print("Sharks has gills and scales")
class Coral(Aquatic):
    def __init__(self):
        print("I am coral")
    def community(self):
        print("Coral lives in community")
    def move(self):
        print("Corals don't show any movement")
class Anemone(Aquatic):
    def __init__(self):
        print("I am Anemone")
    def protect(self):
        print("Anemone protects the clownfish")
class Starfish(Aquatic):
    def __init__(self):
        print("I am starfish")
    def body(self):
        print("Starfish has star like body")
    def move(self):
        print("Starfish has no movements")
s1 = Shark()
s1.place()
s1.swim()
s1.body()
c1 = Coral()
c1.place()
c1.community()
c1.move()
a1 = Anemone()
a1.place()
a1.protect()
f1 = Starfish()
f1.place()
f1.body()
f1.move()

