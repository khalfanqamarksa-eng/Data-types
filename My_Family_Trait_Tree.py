class FamilyTree:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm
    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Height (cm):", self.height_cm)
class Kid(FamilyTree):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.height_cm = height_cm
        super().show_traits()
    def hobby(self):
        print(self.name, "hobby is learning")
    def hobby2(self):
        print(self.name, "hobby is playing football")
    def Class(self):
        print("Hello, My name is", self.name,"My favorite color is", self.eye_color)
child= Kid("Kulfi", 13, "Brown", 135)
child.show_traits()
child.hobby()
child2= Kid("Tom", 15, "Green", 150)
child2.show_traits()
child2.hobby2()
child3= Kid("Jerry", 10, "Blue", 120)
child3.show_traits()
child3.Class()
