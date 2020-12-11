class FarmAnimal:
    def __init__(self, type='Animal', legNumber=0):
        self.type = type
        self.legNumber = legNumber
    def setLeg(self, legNumber):
        self.legNumber = legNumber
    def getLeg(self):
        return self.legNumber
    def describe(self):
        print("%s has %d legs, it lives on the farm." %(self.type, self.legNumber))
class Duck(FarmAnimal):
    def makeSound(self):
        print("Quark! Quark! Quark!")
duck = Duck()     #create a Duck instance
print(duck.legNumber)  # variable defined in parent class
duck.setLeg(2)  #access parent method
print(duck.legNumber)
duck2 = Duck('Duck', 2)  #another duck instance
duck2.describe()   #Duck has 2 legs, it lives on the farm
duck2.makeSound()   #Quark! Quark! Quark!
class Cow(FarmAnimal):
    def __init__(self, type='FarmAnimal', legNumber=4):
        self.type = 'Cow'
        self.legNumber = legNumber
    def makeSound(self):
        print("Moo! Moo! Moo!")
    def getLeg(self):
        if self.legNumber != 4:
            return "Holy Cow! A Cow with %d legs!" %(self.legNumber)
        else:
            return self.legNumber
cow = Cow()
print(cow.legNumber)
cow.describe()
cow.setLeg(2)
print(cow.getLeg())
