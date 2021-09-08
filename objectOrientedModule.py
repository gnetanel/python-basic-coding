def dummy():
    print("dummy")


class Animal:
    name = None
    animalType = "Empty type"

    def __init__(self, name):
        self.name = name

    def printMe(self):
        print("My name is " + self.name)
        print("My type is " + self.animalType)

    def printMe2(self):
        print("printme2 of animal class")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(self, name)
        self.animalType = 'Dog'

    def printMe2(self):
        print("printme2 of animal Dog class")


def execute_me():
    my_dog = Dog("Lucky2")
    my_animal = Animal("Lucky1")

    my_dog.printMe()
    my_dog.printMe2()
    my_animal.printMe()
    my_animal.printMe2()


def dummy():
    print("dummy method")
