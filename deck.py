import random
from card import Card

class Deck:
    """Class defining the attributes of a deck"""

    def shuffle(self):
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
        NUM_SINGLE_GREEN  = 6
        NUM_DOUBLE_GREEN  = 3
        NUM_SINGLE_BLUE   = 6
        NUM_DOUBLE_BLUE   = 4
        NUM_SINGLE_ORANGE = 6
        NUM_DOUBLE_ORANGE = 3
        NUM_SINGLE_RED    = 6
        NUM_DOUBLE_RED    = 4
        NUM_SINGLE_YELLOW = 6
        NUM_DOUBLE_YELLOW = 4
        NUM_SINGLE_PURPLE = 5
        NUM_DOUBLE_PURPLE = 4
        self.cards = []
        self.current_card_idx = 0
        
        # Build the deck
        for i in range(NUM_SINGLE_GREEN):
            self.cards.append(Card('green'))
        for i in range(NUM_DOUBLE_GREEN):
            self.cards.append(Card('green', 2))
        for i in range(NUM_SINGLE_BLUE):
            self.cards.append(Card('blue'))
        for i in range(NUM_DOUBLE_BLUE):
            self.cards.append(Card('blue', 2))
        for i in range(NUM_SINGLE_ORANGE):
            self.cards.append(Card('orange'))
        for i in range(NUM_DOUBLE_ORANGE):
            self.cards.append(Card('orange', 2))
        for i in range(NUM_SINGLE_RED):
            self.cards.append(Card('red'))
        for i in range(NUM_DOUBLE_RED):
            self.cards.append(Card('red', 2))
        for i in range(NUM_SINGLE_YELLOW):
            self.cards.append(Card('yellow'))
        for i in range(NUM_DOUBLE_YELLOW):
            self.cards.append(Card('yellow', 2))
        for i in range(NUM_SINGLE_PURPLE):
            self.cards.append(Card('purple'))
        for i in range(NUM_DOUBLE_PURPLE):
            self.cards.append(Card('purple', 2))

        # Special cards
        self.cards.append(Card('cupcake'))
        self.cards.append(Card('ice_cream'))
        self.cards.append(Card('gummy'))
        self.cards.append(Card('gingerbread'))
        self.cards.append(Card('lollipop'))
        self.cards.append(Card('popsicle'))
        self.cards.append(Card('chocolate'))
        
        # Shuffle the deck
        random.shuffle(self.cards)

    def print(self):
        for i in range(len(self.cards)):
            self.cards[i].print()
