from cards import Card 
from deck import Deck

deal_amount = []

def lucky_card():
    d = Deck()
    d.shuffle()
    try:
        user = input("Hello! What's your name? ")
        deal_amount = int(input(f"How many random cards would you like to be dealt {user}? "))
        if deal_amount >= 53:
            print("There are only 52 cards in a deck!")
        elif deal_amount == 1:
            print(f"Here is your lucky card {user} ", d._deal(deal_amount))
        elif deal_amount <= 1:
            print("You have to enter positive number, there isn't a negative suit.")
        elif 52 >= deal_amount > 1:
            print(f"Here are your {deal_amount} lucky cards {user}", d._deal(deal_amount))
    except ValueError:
        print("Next Time Enter a Number!")
lucky_card()


#CODE BELOW WAS ME TROUBLE SHOOTING AND I DECIDED TO INCLUDE IT IN THIS FILE
#LEARNING OOP HAS BEEN FUN AND I WANT TO LOOK BACK AT MISTAKES. 

# def user_name():
#     user = input("Hello! What's your name? ")
#     deal_amount = int(input(f"How many random cards would you like to be dealt {user}? "))
#     if deal_amount > 52:
#         print("There are only 52 cards in a deck!")
#     return deal_amount

# d = Deck()
# d.shuffle()

# # x 

# print("Here are your ", user_name(), " lucky cards! ", d._deal(user_name()))

# print(user_name())
# print(f"There are {user_name()} cards left in the thing")



# The below code I could not get to display the ValueError code. 

# def lucky_card():
#     d = Deck()
#     d.shuffle()
#     user = input("Hello! What's your name? ")
#     deal_amount = int(input(f"How many random cards would you like to be dealt {user}? "))
#     if deal_amount == ValueError:
#         print("You have to enter a number!")
#     elif deal_amount >= 53:
#         print("There are only 52 cards in a deck!")
#     elif deal_amount == 1:
#         print(f"Here is your lucky card {user} ", d._deal(deal_amount))
#     elif deal_amount <= 1:
#         print("You have to enter positive number, there isn't a negative suit.")
#     elif 52 >= deal_amount > 1:
#         print(f"Here are your {deal_amount} lucky cards {user}", d._deal(deal_amount))
# lucky_card()

#tried this too

#   elif deal_amount.isalnum:
#         print("You have to enter a number!")
#   elif deal_amount.isalpha:
#         print("You have to enter a number!")






