import random

# Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"


# Deck class (inherits from Card)
class Deck(Card):
    def __init__(self):
        self.cards = []  # Initialize an empty deck

        # Card values (1–10 + face cards)
        values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Clubs', 'Diamond', 'Spades']

        # Create the full deck
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

        self.shuffle()  # Shuffle after creation

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            print("Deck is empty.")
            return None


# Dealer class (inherits from Deck)
class Dealer(Deck):
    def __init__(self, deck):
        super().__init__()
        self.deck = deck  # Use the deck passed in

    def getDealCard(self):
        return self.deck.deal()

    def isEmpty(self):
        return len(self.deck.cards) == 0


# ======= Execution Section =======
if __name__ == "__main__":
    deck_instance = Deck()
    dealer_instance = Dealer(deck_instance)

    dealt_card = dealer_instance.getDealCard()

    if dealt_card:
        print("Deck is dealt from.")
        print(f"The dealer dealt: {dealt_card}")
    else:
        print("No card was dealt.")


