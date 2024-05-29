import random

def game():
    player_score = 0
    computer_score = 0
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        player_choice = input("Enter rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose: {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
                player_score += 1
            else:
                print("You lose!")
                computer_score += 1
        else:
            print("Invalid choice. Please try again.")
        print(f"Player: {player_score}, Computer: {computer_score}")
        play_again = input("Play again? (yes/no): ")
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    game()

