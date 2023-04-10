import random


# Defining constants for Rock, Scissors and Paper
ROCK = "Rock"
SCISSORS = "Scissors"
PAPER = "Paper"


def play_game():
    # Invite the player to choose one of three possibilities
    print("\033[1;32mChose Rock[r], Scissors[s], or Paper[p]: \033[0m", end='')  # + fg.rs (?!?)
    player_move = input().lower()

    # Turn player input into one of moves options and print it
    while player_move not in ["r", "s", "p"]:
        print("\033[1;31mInvalid Input. Try again...\033[0m")
        print("\033[1;32mChose Rock[r], Scissors[s], or Paper[p]: \033[0m", end='')
        player_move = input().lower()
    if player_move == "r":
        player_move = ROCK
    elif player_move == "s":
        player_move = SCISSORS
    elif player_move == "p":
        player_move = PAPER

        # raise SystemExit("\033[1;31mInvalid Input. Try again...\033[0m")
    print(f"\033[1;94mYou chose {player_move}.\033[0m")

    # Choose random Computer's move
    computer_move = random.randint(1, 3)

    # Turn Computers random choose into one of moves options and print it
    if computer_move == 1:
        computer_move = ROCK
    elif computer_move == 2:
        computer_move = SCISSORS
    elif computer_move == 3:
        computer_move = PAPER
    print(f"\033[1;95mThe computer chose {computer_move}.\033[0m")

    # Check and print the result
    if (player_move == ROCK and computer_move == SCISSORS) or \
            (player_move == SCISSORS and computer_move == PAPER) or \
            (player_move == PAPER and computer_move == ROCK):
        print("\033[1;30;102m You win! \033[0m")
    elif player_move == computer_move:
        print("\033[1;30;103m Draw! \033[0m")
    else:
        print("\033[1;30;101m You lose! \033[0m")


def play_again():
    print("\033[1;32mPlay again? Yes(y) or No(n): \033[0m", end='')
    while True:
        again = input().lower()
        if again == "y":
            return True
        elif again == "n":
            return False
        else:
            print("\033[1;31mInvalid Input. Try again...\033[0m")
            print("\033[1;32mPlease chose Yes(y) or No(n): \033[0m", end='')


while True:
    play_game()
    if not play_again():
        break
