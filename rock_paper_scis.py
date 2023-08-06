import random
import time

# Input options for game
player_choices = ["rock","paper", "scissors"]

# Start the game
def main():
        try:
            print("Welcome to Rock Paper Scissors!")
            time.sleep(1)
            player_1_rcs = input("Please choose Rock, Paper, or Scissors: ").lower
                  
            # Check if the player entered a valid choice
            while player_1_rcs not in player_choices:
                print("Invalid choice. Please choose Rock, Paper, or Scissors.")
                player_1_rcs = input("Please choose Rock, Paper, or Scissors: ").lower()

            computer_choice = random.choice(player_choices)

            print(f"Opponent chose: {computer_choice.capitalize()}")

            check_winner(player_1_rcs, computer_choice)

            new_game()

        except (ValueError, NameError, TypeError):
            print("Please enter a valid input.")

# Check who won the game.
def check_winner(player_choices, computer_choice):
    if player_choices == computer_choice:
        print("Tie!")
    elif (player_choices == "rock" and computer_choice == "scissors") or \
    (player_choices == "paper" and computer_choice == "rock") or \
    (player_choices == "scissors" and computer_choice == "paper"):
        print("You Win!")
    else:
        print("Your opponent won this one!")

# Ask the user if they would like to play again.
def new_game():
    while True:
        want_play_again = input("Would you like to play again? (yes/no) ").lower()
        if want_play_again == "no":
            print("Thank you for playing!")
            exit()
        elif want_play_again == "yes":
            print("Starting a new game...")
            main()
            break  # Exit the loop to start a new game
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Run Game
if __name__ == "__main__":
    main()


