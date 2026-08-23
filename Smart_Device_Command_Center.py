from abc import ABC, abstractmethod


# Abstract Base Class
class SmartDevice(ABC):

    def __init__(self, device_name):
        self.device_name = device_name

    @abstractmethod
    def operate(self):
        pass


# Concrete Classes overriding operate()
class SmartLight(SmartDevice):

    def operate(self):
        return f"{self.device_name}: Adjusting brightness to 80%."


class SmartThermostat(SmartDevice):

    def operate(self):
        return f"{self.device_name}: Setting temperature to 72°F."


# Polymorphism in action
devices = [
    SmartLight("Living Room Light"),
    SmartThermostat("Main Thermostat"),
    SmartLight("Bedroom Light"),
]

for device in devices:
    print(device.operate())