# Rock, Paper, Scissors Game
from random import randint

# Moves for player
moves = ["rock", "paper", "scissors"]

# Boolean Loop
while True:
    computer = moves[randint(0,2)]
    player = input("Rock,Paper or Scissors? (Or End Game?) ").lower()
    if player == "end game":
        print("The game has ended!")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
        print("Check your spelling...")

