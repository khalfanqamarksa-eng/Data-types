amount = int(input("Input the Amount for withdrawal: "))
note_1 = amount//100
remainder1 = amount%100
note_2 = remainder1//50
remainder2 = remainder1%50
note_3= remainder2//10
print ("The number of 100 notes is", note_1)
print ("The number of 50 notes is", note_2)
print ("The number of 10 notes is", note_3)