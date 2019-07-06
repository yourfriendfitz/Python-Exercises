import random

def RPS():
    print("Rock")
    print("Paper")
    print("Scissors")
RPS()

random_draw = random.randint(1,3)

if random_draw == 1:
    player2 = "rock"
elif random_draw == 2:
    player2 = "paper"
elif random_draw == 3:
    player2 = "scissors"

player1 = input("Player 1 Enter your Selection: ")
print(f"Player 2 Drew {player2}")
   
player1 = player1.lower()
player2 = player2.lower()

if player1 == player2:
    print("It's a Tie!")
elif player1 == "rock":
    if player2 == "paper":
        print("Player 2 Wins")
    elif player2 == "scissors":
        print("Player 1 Wins")
    else:
        print("Player 2 made an invalid entry.")
elif player1 == "paper":
    if player2 == "scissors":
        print("Player 1 Wins")
    elif player2 == "rock":
        print("Player 2 Wins")
    else:
        print("Player 2 made an invalid entry.")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 Wins")
    elif player2 == "rock":
        print("Player 2 Wins")
    else:
        print("Player 2 made an invalid entry.")
else:
    print("Your selection was not valid.")

