"""
Question 2: Card Dealer
Group Member: Riley Barrett
"""

import random


# Creating class for individual cards
class Cards:
    # Setting the suits and ranks as a string
    def __init__(self):
        self.suits: str
        self.ranks: str


# Making a class for the deck
class Deck:
    # setting the actual deck
    def __init__(self):
        self.deck = []
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.__get_deck__()

    # A definition for what the user will see and making sure
    # they cant implement an incorrect amount wile giving a remainder
    def user(self):
        while True:
            print("I have shuffled a deck of 52 cards")
            num_of_cards = int(input("\nHow many cards would you like: "))
            if num_of_cards > 52 or num_of_cards < 0:
                print("Pick a number between 1 and 52")
                continue
            player_cards = []
            for i in range(num_of_cards):
                player_cards.append(self.deck.pop())
            remainder = 52 - num_of_cards
            for card in player_cards:
                print(card)
            print(f"\nYou have {remainder} cards left in the deck")
            print("bye!")
            break

    # Displays the greeting message
    def greeting(self) -> str:
        print("Card Dealer".center(50, "-"))
        print("")

    # Shuffles the deck of cards
    def shuffle_cards(self):
        random.shuffle(self.deck)

    # Getting the cards or card from the deck
    def __get_deck__(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = f"{rank} of {suit}"
                self.deck.append(card)

    # Returning a string from the deck to display what card you got
    def __str__(self) -> str:
        return str(self.deck)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle_cards()

deck.greeting()
deck.shuffle_cards()
deck.user()
