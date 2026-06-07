def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x/y
def calculator():
    print("Welcome to the Function Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter your choice (1, 2, 3, 4):")
        if choice == '5':
            print("Exiting calculator.")
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter the second number:"))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    print("Division by zero is not possible.")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
if __name__ == "__main__":
    calculator()
                