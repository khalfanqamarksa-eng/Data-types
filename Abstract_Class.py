from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed Value:", x)
    @abstractmethod
    def task(self):
        print("We are in inside Abstract Class task")
class test_Class(Absclass):
    def task(self):
        print("We are in inside Abstract Class task")
obj1 = test_Class()
obj1.task()
obj1.print(100)

