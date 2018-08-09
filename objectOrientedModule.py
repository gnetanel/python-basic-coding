def dummy():
    print("dummy")

class Animal():
    name = None
    animalType = "Empty type"
    def __init__(self, name):
        self.name=name

    def printMe(self):
        print("My name is " + self.name)
        print("My type is " + self.animalType)

    def printMe2(self):
        print("printme2 of animal class")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.animalType = 'Dog'

    def printMe2(self):
        print("printme2 of animal Dog class")

def runme():
    myDog = Dog("Lucky2");
    myAnimal = Animal("Lucky1");

    myDog.printMe()
    myDog.printMe2()
    myAnimal.printMe()
    myAnimal.printMe2()

def dummy():
    print("dummy method")
