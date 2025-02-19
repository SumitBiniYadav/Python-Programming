# Parent class
class Vehicle:
    def general_info(self):
        return "Vehicles are used for transportation"

# Child class 1
class Car(Vehicle):
    def wheels(self):
        return "Car has 4 wheels"

# Child class 2
class Bike(Vehicle):
    def wheels(self):
        return "Bike has 2 wheels"

# Create instances
car = Car()
bike = Bike()

print(car.general_info())  # Inherited from Vehicle
print(car.wheels())        # Car-specific method
print(bike.general_info()) # Inherited from Vehicle
print(bike.wheels())       # Bike-specific method
