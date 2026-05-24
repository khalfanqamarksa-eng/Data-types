def cube_of_cube(number):
    if number%3==0:
        return number**3
    else:
        return "The number is not a multiple of 3"
number =int(input("Enter a number:"))
print(cube_of_cube(number))

            