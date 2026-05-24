def factorial(x):
    """This function shows the factorial of a number"""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial.__doc__)
number = int(input("Enter a number:"))
print("The factorial of this number is:", factorial(number))
