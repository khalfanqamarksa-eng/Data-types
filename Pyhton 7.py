a = 10
b = 12
c = 0
if a > 0 and b > 0 and c > 0:
    print ("All numebers have value of true")
else:
    print ("At least one of the numbers has value of false")
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print ("At least one of the numbers is greater than zero")
else:
        print ("None of the numbers is greater than zero")
if b > 0 or c > 0:
    print ("At least one of the numbers is greater than zero")
else:
        print ("None of the numbers is greater than zero")
a = 10
b = 5
c = 0
if a > 0 and not b > 0:
    print ("Only one number is greater than zero")
else:
    print ("Both numbers are greater than zero or both numbers are not greater than zero")