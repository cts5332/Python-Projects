import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input, please try again")
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]    
    # 0 is rock
    # 1 is paper
    # 2 is scissors
    print("computer picked", computer_choice +".")

    if computer_choice == user_input:
        print("The game is a tie")

    elif computer_choice == "paper" and user_input == "rock":
        print("Computer wins")
        computer_wins += 1

    elif computer_choice == "scissors" and user_input == "rock":
        print("You win")
        user_wins += 1

    elif computer_choice == "rock" and user_input == "paper":
        print("You win")
        user_wins += 1
    
    else:
        print("Computer wins")
        computer_wins += 1

print("User wins",user_wins)
print("Computer wins",computer_wins)