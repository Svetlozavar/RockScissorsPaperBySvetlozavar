import random
# Defining variables for Rock, Scissors and Paper
rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

# Invite the player to choose one of three possibilities
player_move = input("Choise [r]ock, [s]cissors, or [p]aper: ")

# Turn player input into one of moves options and print it
if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    raise SystemExit("Invalid Input. Try again...")
print(f"You chose {player_move}.")

# Choose random Computer's move
computer_move = random.randint(1, 3)

# Turn Computers random choose into one of moves options and print it
if computer_move == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = scissors
elif computer_move == 3:
    computer_move = paper
print(f"The computer chose {computer_move}.")

# Check and print the result
if (player_move == rock and computer_move == scissors) or \
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
