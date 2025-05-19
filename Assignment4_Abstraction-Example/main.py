from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    # Abstract method to be implemented by subclasses
    @abstractmethod
    def move(self):
        pass

# Concrete class Car that inherits from Vehicle
class Car(Vehicle):
    def move(self):
        return 'The car moves on the road.'

# Concrete class Boat that inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        return 'The boat sails on the water.'

# Creating objects of each subclass
car = Car()
print(car.move())   

boat = Boat()
print(boat.move())  
