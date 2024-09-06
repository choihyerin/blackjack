class Deck:
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

     def __repr__(self):
         return f"{self.rank} of {self.suit}"
