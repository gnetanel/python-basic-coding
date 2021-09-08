from car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 11

    def describe_battery(self):
        print("My battery is", self.battery, "years old")
