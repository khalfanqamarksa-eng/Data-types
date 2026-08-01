class MyClass:
    __privateVar=27
    def __privateMeth(self):
        print("I am inside class MyClass")
    def hello(self):
        print("private variable value:",MyClass.__privateVar)
obj1= MyClass()
obj1.hello()