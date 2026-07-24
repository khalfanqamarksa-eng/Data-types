class dogs:
    Breed = "Golden Retriever"
    Breed1 = "Labrador Retriever"
    Breed2 = "German Shepherd"
    def __init__(self,name, age, color):
        self.name = name
        self.age = age
        self.color = color
obj1 = dogs("Cupcake", 2, "Golden")
obj2 = dogs("Max", 7, "Brown")
obj3 = dogs("Rocky", 1, "Black")
print("Name :", obj1.name)
print("Age :", obj1.age)
print("Color :", obj1.color)
print("Breed {}".format(obj1.Breed))
print("Name :", obj2.name)
print("Age :", obj2.age)
print("Color :", obj2.color)
print("Breed {}".format(obj2.Breed1))
print("Name :", obj3.name)
print("Age :", obj3.age)
print("Color :", obj3.color)
print("Breed {}".format(obj3.Breed2))
