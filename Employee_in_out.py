class employee():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called")
    def create_object(self):
        print("Making object")
        obj1 =employee()
        print("Function ended")
        return obj1
print("Calling create_obj() function")
obj1 = employee().create_object()
print("Program Ended")