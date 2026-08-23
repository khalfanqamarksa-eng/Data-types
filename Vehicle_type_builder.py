class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}"


class Car(Vehicle):

    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Use super()
        self.doors = doors

    # Overriding parent method
    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Doors: {self.doors}"


# Test instance
my_car = Car("Toyota", "Camry", 4)
print(my_car.get_info())

# Checking relationship with issubclass()
print(f"Is Car a subclass of Vehicle? {issubclass(Car, Vehicle)}")