string = input("Please enter a string: ")
string2 = (' ')
for i in string:
    string2 = i + string2
for i in string2:
    string3 = i + string3
print("The original string is: ", string)
print("The reverse of the string is: ", string2)