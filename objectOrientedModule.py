def dummy():
    print("dummy")

class Animal():
    name = None
    animalType = None
    def __init__(self, name):
        self.name=name

    def printMe(self):
        print("My name is " + self.name)
        print("My type is " + self.animalType)

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.animalType = 'Dog'


def runme():
    myDog = Dog("Lucky");
    myDog.printMe()

