import random

def RPS():
    print("Rock")
    print("Paper")
    print("Scissors")
RPS()

random_draw = random.randint(1,3)

if random_draw == 1:
    player2 = "Rock"
elif random_draw == 2:
    player2 = "Paper"
elif random_draw == 3:
    player2 = "Scissors"

player1 = input("Player 1 Enter your Selection: ")
print(f"Player 2 Drew {player2}")
   
player1 = player1.capitalize()
player2 = player2.capitalize()

if player1 == player2:
    print("It's a Tie!")
elif player1 == "Rock":
    if player2 == "Paper":
        print("Player 2 Wins")
    elif player2 == "Scissors":
        print("Player 2 Wins")
    else:
        print("Player 2 made an invalid entry.")
elif player1 == "Paper":
    if player2 == "Scissors":
        print("Player 1 Wins")
    elif player2 == "Rock":
        print("Player 2 Wins")
    else:
        print("Player 2 made an invalid entry.")
elif player1 == "Scissors":
    if player2 == "Paper":
        print("Player 1 Wins")
    elif player2 == "Rock":
        print("Player 2 Wins")
    else:
        print("Player 2 made an invalid entry.")
else:
    print("Your selection was not valid.")

