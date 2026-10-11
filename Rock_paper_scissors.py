import random

choices = ["rock", "paper", "scissors"]
rematch = True

while rematch:
    computer = random.choice(choices)
    user_choice = input("Please choose rock, paper, or scissors: ").lower().strip()

    while user_choice not in choices:
        print("Invalid choice, please choose again.")
        print(choices)
        user_choice = input("Please choose rock, paper, or scissors: ").lower().strip()

    print("Computer chose: " + computer)
    if user_choice == computer:
        print("It's a draw.")
    else:
        if user_choice != computer:
            print("you win")
        else:
            print("lose you oppenet played" "" + computer)

    play_again_choice = input("Play again? (yes/no): ").lower().strip()
    if play_again_choice == "yes":
        rematch = True
    else:
        rematch = False