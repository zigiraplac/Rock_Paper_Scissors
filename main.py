""" This a game Rock Paper Scissors Lizard"""
import random
playing = True
options = ('rock', 'paper', 'scissors')

while playing:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Choose your option (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing!")

