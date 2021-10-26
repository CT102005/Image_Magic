# classes_exercise.py

# """
#1. Create a class according to the following requirements:
#It's name is Vehicle and it has the following attributes/methods:
#Attributes/properties:
#  name: str
#  max_speed: int
#  capacity: int
#Methods:
#    vroom() -> None
#        Prints "Vroom" max_speed times
#2. Create a child/subclass of Vehicle called Bus with the following methods:
#Methods:
#    fare(age: float) -> None
#        Prints "The fare of the bus ride is {}."
#            Price depends on age:
#                0-17 years - Free
#                18-60 years - $5
#                61+ years - Free
#"""

class Vehicle:
    """ Represents a vehicle which goes VROOM
    Attributes:
        name: A string of the name
        max_speed: An integer of the maximum speed of the vehicle in km/h
        capacity: An integer of the capacity of the vehicle
    """

    def __init__(self, name: str, max_speed: int, capacity: int) -> None:
        """Creates a new vehicle with default values.

        Args:
            name: str
                the name of the vehicle
            max_speed: int
                the maximum speed of the vehicle
            capacity: int
                the capacity of the vehicle
            """
        self.name = "Car"
        self.max_speed = 50
        self.capacity = 5

    def vroom(self) -> None:
        """Returns the number of vrooms the vehicle creates"""
        for i in range(self.max_speed):
            print("vroom")

class Bus(Vehicle):
    """Represents a bus which IS A VEHICLE"""
    def fare(self, age: float) -> None:
        """Description
        Args:
            age: the age of the person riding the bus
        Returns:
              The fare for the person entering the bus, based on their age
        """
        if age >= 18:
            if age <= 60:
                print("The fare of the bus ride is $5")
        elif age >= 17:
            print("The fare of the bus ride is free.")
        else:
            print("The fare of the bus ride is free.")

some_bus = Bus("bus", 60, 20)
some_bus.fare(10)

some_vehicle = Vehicle("car", 50, 10)
some_vehicle.vroom()

