# Rules of the Game:
# - The player and the computer each choose one of three options: Rock, Paper, or Scissors.
# - Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
# - If both choose the same option, it's a tie.

import random
# ASCII Art for Rock, Paper, and Scissors
Rock ="""
     _______
----'   ____|
       (_____| 
 ROCK  (_____| 
       (____) 
----.__(___) 
"""
Paper="""
       _______
-----'    ____)____
             ______)
 PAPER      _______)
           _______)
----.__________) 
"""
Scissors="""
    _______
---'   ____)_____
            _____)__ 
SCISSORS   _________)
       (____)
---.___(___)
"""

# Initialize player variable and available options
player = None
options = ("rock", "paper", "scissors")
running = True  # Game runs as long as this is True

while running:
    # Computer selects a random choice from the options
    computer_choice = random.choice(options)
    
    while True:
        # Ask the player for their choice and validate input
        player_choice = input("Move your choice: Rock, Paper or Scissors?").lower()
        if player_choice in options:  # Ensure valid input
            break

    choices = {
        'rock': Rock, 
        'paper': Paper, 
        'scissors': Scissors
    }
    
    print("Computer's Choice: ", choices.get(computer_choice))
    print("Player's Choice: ", choices.get(player_choice))

    # Determine the winner based on the choices
    if (player_choice == computer_choice):
        print("It's a tie.")
    elif (player_choice == "rock" and computer_choice == "scissors"):
        print("You Won!")
    elif (player_choice == "paper" and computer_choice == "rock"):
        print("You Won!")
    elif (player_choice == "scissors" and computer_choice == "paper"):
        print("You Won!")
    else:
        print("You Lose!")

    # Ask the player if they want to play again
    if not input("Do you want to play again? (Press Enter to play again)").lower() == "":
        running = False  # End the game if the player doesn't press Enter

# Display a message after the game ends
print("Thanks for playing! Hope to see you again soon!")
