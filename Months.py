def january():
    print("This is January")
def february():
    print("This is February")
def march():
    print("This is March")
def april():
    print("This is April")
def may():
    print("This is May")
def june():
    print("This is June") 
def july():
    print("This is July")
def august():
    print("This is August")
def september():
    print("This is September")
def october():
    print("This is October")
def november():
    print("This is November")
def december():
    print("This is December")  
print("Hello!, Today you will learn about the months of the year")

try:
    answer = int(input("First can you guess how many months are there in a year?"))
    if answer == 12:
        print("Correct!")
    else:
        print("Incorrect!, No there are 12 months in a year.")
except ValueError:
    print("Please enter a valid number.")