from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.values = ["Ace", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(value, suit)
                      for suit in self.suits for value in self.values]
        # Below nested for loops would work, but the better way to do it is above
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)


class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.cards = self.deck.cards
        self.deal_amount = []

    def count(self):
        return len(self.cards)

    def _deal(self, num):
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

    def lucky_card(self, user):
        playing = True
        while playing:
            try:
                deal_amount = int(
                    input(f"How many random cards would you like to be dealt {user}? "))
                if deal_amount >= 53:
                    print("There are only 52 cards in a deck!")
                elif deal_amount == 1:
                    print(f"Here is your lucky card {user} ", self._deal(
                        deal_amount))
                elif deal_amount <= 1:
                    print("You have to enter positive number, there isn't a negative suit.")
                elif 52 >= deal_amount > 1:
                    print(f"Here are your {deal_amount} lucky cards {user}", self._deal(
                        deal_amount))
            except ValueError:
                print("Next Time Enter a Number!")
            keep_playing = input("Press enter or any key to play again\nPress q to quit: ")
            if keep_playing == "q":
                print("Goodbye")
                playing == False
                break

    def twenty_one(self, user):
        playing = True
        while playing:
            try:
                deal_amount = 2
                if deal_amount >= 53:
                    print("There are only 52 cards in a deck!")
                elif deal_amount == 1:
                    print(f"Here is your lucky card {user} ", self._deal(
                        deal_amount))
                elif deal_amount <= 1:
                    print("You have to enter positive number, there isn't a negative suit.")
                elif 52 >= deal_amount > 1:
                    print(f"Here are your {deal_amount} lucky cards {user}", self._deal(
                        deal_amount))
            except ValueError:
                print("Next Time Enter a Number!")
            keep_playing = input("Press enter or any key to play again\nPress q to quit: ")
            if keep_playing == "q":
                print("Goodbye")
                playing == False
                break
    

    def play(self, user):
        choosing_game = True
        while choosing_game:
            try:
                game_choice = (
                    input(f"What game would you like to play {user}?\n1 - lucky card\n2 - Twenty One\nType q to quit: "))
            except:
                print("Please enter a number associated with a game only!")
            if game_choice == "q":
                choosing_game = False
                print("Goodbye")
                return
            if int(game_choice) == 1:
                choosing_game = False
                self.lucky_card(user)
            if int(game_choice) == 2:
                choosing_game = False
                self.twenty_one(user)


app_running = True
while app_running:
    user = input("Hello! What's your name? ")
    dealer = Dealer()
    dealer.shuffle()
    dealer.play(user)
    app_running = False
