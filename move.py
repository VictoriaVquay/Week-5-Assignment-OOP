# Base class for Vehicle
class Vehicle:
    # Base move() method
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car class inheriting from Vehicle
class Car(Vehicle):
    # Override move() to print driving action
    def move(self):
        return "Driving "

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    # Override move() to print flying action
    def move(self):
        return "Flying "

# Base class for Animal
class Animal:
    # Base move() method
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Dog class inheriting from Animal
class Dog(Animal):
    # Override move() to print running action
    def move(self):
        return "Running "

# Bird class inheriting from Animal
class Chameleon(Animal):
    # Override move() to print flying action
    def move(self):
        return "Walk slowly "

# Testing the classes
def test_movement():
    # Create instances of each class
    car = Car()
    plane = Plane()
    dog = Dog()
    chameleon = Chameleon()

    # List of Vehicles
    vehicle = [car, plane]

    # Loop through each animal and call move()
    for vehicle in vehicle:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

     # List of animals
    animals = [dog, chameleon]

    # Loop through each animal and call move()
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.move()}")
        
# Call the test function
test_movement()
