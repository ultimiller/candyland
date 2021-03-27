class Card:
    """Class defining the attributes of a card"""
    
    def __init__(self, color, num_squares=1):
        self.color = color
        self.num_squares = num_squares
        # Mark 'special' cards that jump to a specific space
        if (color in ['green', 'blue', 'orange', 'red', 'yellow', 'purple']):
            self.special = False
        else:
            self.special = True

    def print(self):
        s = ""
        if (self.num_squares == 2):
            s = self.color + " "
        s = s + self.color
        print(s)
