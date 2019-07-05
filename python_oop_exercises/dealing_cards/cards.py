#create a card class
#each card need a value Ace through King
#each cards needs a suit Hearts, Spades, Diamonds, and clubs

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 

    def __repr__(self):
        return f"{self.value} of {self.suit}"
