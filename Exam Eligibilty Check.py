medicalcause= (input("Do you have a medical cause? (Y/N)")).strip () . upper ()
if medicalcause == "Y":
    print("Allowed")
else:
    atten1 =int(input ("What is your attendace?"))
    if atten1 >= 75:
        print("Allowed")
    else:
        print("Not Allowed")