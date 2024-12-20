import random

choices = ["rock", "paper", "scissors"]
print("Welcome to the rock, paper, scissors game!")
print("Good luck!")

while True:
    user_choice = input("Please enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Please enter a valid choice.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
    