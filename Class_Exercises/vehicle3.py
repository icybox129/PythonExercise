# 3) Create a child class Bus that will inherit all of the variables and methods of the 1st Vehicle class
# 4) Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.

class Vehicle:
    def __init__(self, max_speed, mileage, colour):
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour
    

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, colour, horsePower):
        super().__init__(max_speed, mileage, colour)
        self.horsePower = horsePower

Bus1 = Bus(80, 35000, "Yellow", "450 BHP")

print(Bus1.max_speed, Bus1.mileage, Bus1.colour, Bus1.horsePower)