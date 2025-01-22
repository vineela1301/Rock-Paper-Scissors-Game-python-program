import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Main function for the game
def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, or scissors (or type 'quit' to exit)")
        user_choice = input("Your choice: ").lower()

        # Exit condition
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display choices and result
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display current scores
        print(f"Current score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Final scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
