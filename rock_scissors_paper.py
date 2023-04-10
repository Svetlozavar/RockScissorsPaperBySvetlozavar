import random

# Defining variables for Rock, Scissors and Paper
rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

# Invite the player to choose one of three possibilities

print("\033[1;32mChose [r]ock, [s]cissors, or [p]aper: \033[0m", end='')  # + fg.rs (?!?)
player_move = input().lower()

# Turn player input into one of moves options and print it
if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    raise SystemExit("\033[1;31mInvalid Input. Try again...\033[0m")
print(f"\033[1;94mYou chose {player_move}.\033[0m")

# Choose random Computer's move
computer_move = random.randint(1, 3)

# Turn Computers random choose into one of moves options and print it
if computer_move == 1:
    computer_move = rock
elif computer_move == 2:
    computer_move = scissors
elif computer_move == 3:
    computer_move = paper

print(f"\033[1;95mThe computer chose {computer_move}.\033[0m")

# Check and print the result
if (player_move == rock and computer_move == scissors) or \
        (player_move == scissors and computer_move == paper) or \
        (player_move == paper and computer_move):
    print("\033[1;30;102m You win! \033[0m")
elif player_move == computer_move:
    print("\033[1;30;103m Draw! \033[0m")
else:
    print("\033[1;30;101m You lose! \033[0m")
