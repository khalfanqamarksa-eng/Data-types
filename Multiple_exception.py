try:
    num1, num2 =eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is an error.")
except SyntaxError:
    print("There is no comma.")
except:
    print("Wrong input.")
else:
    print("No exception occurred.")
    