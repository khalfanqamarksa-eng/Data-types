def tip_waiter(bill, tip):
    return bill + tip
bill = int(input("Enter the bill amount: "))
tip= int(input("Enter the tip amount: "))
print ("Total Amount is :" , tip_waiter(bill, tip))
