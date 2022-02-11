#7) Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#Note: The bus seating capacity is 50. so the final fare amount should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.

class Vehicle:
    seating_capacity = 50

    def __init__(self, colour, maxSpeed, mileage, horsePower):
        self.colour = colour
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.horsePower = horsePower
    
class Bus(Vehicle):

    fare = Vehicle.seating_capacity * 100
    total_fare = (fare / 10) + fare 

    def __init__(self, colour, maxSpeed, mileage, horsePower):
        super().__init__(colour, maxSpeed, mileage, horsePower)
    
Bus1 = Bus("Red", 250, 35000, "500 BHP")
print("Total fare for this bus trip is: £{}" .format(Bus1.total_fare))
print("Customer: Wow, that's expensive!")
