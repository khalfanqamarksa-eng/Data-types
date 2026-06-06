import random
while True:
    user_action =input("Enter a choice(Rock.Paper, Scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"Draw! Both players selected {user_action}.")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("You win!")
        else:
            print("You lose!")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("You win!")
        else:
            print("You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
    
    