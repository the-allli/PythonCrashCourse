class Car:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand  # attribute
        self.model = model

    def drive(self):  # method
        print(f"{self.brand} {self.model} is driving.")

# create an object
my_car = Car("Toyota", "Corolla")
my_car.drive()
