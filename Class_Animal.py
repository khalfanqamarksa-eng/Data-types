from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Parrot(Animal):
    def move(self):
        print("Parrots can can mimic humans")
class Snake(Animal):
    def move(self):
        print("Some snakes are non-venomous")
class Cheetah(Animal):
    def move(self):
        print("Cheetahs can run fast but they overheat quickly")
obj1 = Parrot()
obj1.move()
obj2 = Cheetah()
obj2.move()
