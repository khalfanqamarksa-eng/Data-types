class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
obj = vehicle(240, 18)
print("Maximum Speed is:", obj.max_speed)
print("Mileage is:", obj.mileage)