from car import Car
from electric_car import ElectricCar


# Main function

def print_info(*arg, **kwargs):
    print("In function print_info of main module")
    for car in arg:
        car.print_me()


basic_car = Car('Volvo', 'D9', 2020)
tesla_car = ElectricCar('Tesla', 'TT', 2020)

# basic_car.print_me()
# tesla_car.print_me()
# tesla_car.describe_battery()

print_info(basic_car, tesla_car)
