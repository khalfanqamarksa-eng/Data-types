import random
playing = True
number = str(random.randint(0,9))
print("Welcome to the Number Game!, I will generate a random number between 0 and 9, and you have to guess the number on at a time")
print("The game ends when you guess correctly")
while playing:
    guess = input("Enter a number between 0 and 9: ")
    if number == guess :
        print ("You win!")
        print("The number was ", number)
        break
    else:
        print("Nope, try again!")