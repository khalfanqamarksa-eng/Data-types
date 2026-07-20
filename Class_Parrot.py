class Parrot:
    Species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Green = Parrot("Polly", 3)
Woody = Parrot("Molly", 7)
print("Name of the 1st parrot is", Green.name)
print("Age of the 1st parrot is", Green.age)
print("Green is a {}".format(Green.Species))
print("Name of the 2nd Parrot is:", Woody.name)
print("Age of the 2nd Parrot is:", Woody.age)
print("Woody is a {}".format(Woody.Species))