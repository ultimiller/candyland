import random
from card import Card

class Deck:
    """Class defining the attributes of a deck"""

    def shuffle(self):
        print("Shuffling...")
        random.shuffle(self.cards)

    def draw(self):
        if (self.current_card_idx == len(self.cards)):
            self.current_card_idx = 0
            self.shuffle()

        # Return the next card object and increment
        # current card index
        next_card = self.cards[self.current_card_idx]
        
        self.current_card_idx += 1
        return next_card
        
    def __init__(self):
        NUM_SINGLE_YELLOW = 4
        NUM_DOUBLE_YELLOW = 2
        self.cards = []
        
        # Build the deck
        for i in range(NUM_SINGLE_YELLOW):
            self.cards.append(Card('yellow'))
        for i in range(NUM_DOUBLE_YELLOW):
            self.cards.append(Card('yellow', 2))
        
        #Shuffle the deck
        random.shuffle(self.cards)

    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()
