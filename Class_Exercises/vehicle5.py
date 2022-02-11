# 5) Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, max_speed, mileage, colour, seating_capacity=50):
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour
        self.seating_capacity = seating_capacity
    

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, colour, seating_capacity=100):
        super().__init__(max_speed, mileage, colour, seating_capacity)

Bus1 = Bus(100, 10000, "Red")

print(Bus1.seating_capacity)