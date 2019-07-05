#Deck has a cards attribute with 52 possible instances
#Deck is able to shuffle cards
#Deck is able to deal cards
from cards import Card
from random import shuffle

class Deck:
    def __init__(self):
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
        #Below nested for loops would work, but the better way to do it is above
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)

    def count(self):
        return len(self.cards)

    def _deal (self, num):
        count = self.count()
        actual = min([count, num])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(0)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        shuffle(self.cards)
        return self
    





# d.cards.pop() Testing to make sure it counts one less card
# print(d.count())
# print(d.cards)

