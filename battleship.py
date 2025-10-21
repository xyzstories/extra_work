import random

battleship_grid = [["_"] * 5 for _ in range(5)]
user_hits = 0
computer_hits = 0
def print_grid():
    for row in battleship_grid:
        print(" ".join(row))
input("Welcome to the Battleship Game!")

while True:
    computer_ship = (random.randint(0, 4), random.randint(0, 4))

    user_row = int(input("Pick a row to protect from computer: "))
    user_col = int(input("Pick a column to protect from computer: "))
    user_ship = (user_row, user_col)
    if user_row or user_col not in range(0,4):
        print("Sorry, row or column not available!")

    guess_row = int(input("Choose a row to attack: "))
    guess_col = int(input("Choose a column to attack: "))
    guess = (guess_row, guess_col)

    if guess == computer_ship:
        print("You hit the computer’s ship!")
        battleship_grid[guess_row][guess_col] = "X"
        user_hits += 1
        print(f"You now have {user_hits} points")
    else:
        print("Miss!")
        battleship_grid[guess_row][guess_col] = "O"
    print_grid()

    computer_guess = (random.randint(0, 4), random.randint(0, 4))
    print(f"The computer chose to attack {computer_guess}")
    if computer_guess == user_ship:
        print("The computer hit your ship. Lock in.")
        computer_hits += 1
    else:
        print("The computer missed! Play On!")
    print_grid()

    if user_hits == 5:
        print("Congrats! You won!")
        break
    elif computer_hits == 5:
        print("You lost... Better luck next time")
        break








