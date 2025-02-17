from vehicle import Vehicle  # Importing the Vehicle class

class Car(Vehicle):  # Inheriting from Vehicle
    def __init__(self, wheel_size, wheel_number, make=None):  # make has a default value
        super().__init__(wheel_size, wheel_number)  # Calling the parent constructor
        self.make = make  # New attribute specific to Car

    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"  # Overriding the go() method
