class Board:

    def __init__(self):
        # Keep the ordered colors of each board space in a list for quick
        # searches for the next space after each turn.
        self.colors = ['blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green']

        # Number of spaces before the end (Candy Castle)
        self.num_spaces = len(self.colors)

        # Add one of each color to the end of the board to allow the last
        # move to complete before the end of the game
        self.colors.append(['blue', 'red', 'yellow', 'green'])

        # Set an array for handling lose-a-turn spots
        self.lose_turns = [False for i in range(self.num_spaces)]
        #self.lose_turns[35] = True
        #self.lose_turns[70] = True

        # Set an array for handling shortcuts on the board.
        # Default each space's shortcut value to -1, and for the 2 shortcut spaces
        # set the shortcut value to the board index of the space jumped to.
        self.shortcuts = [-1 for i in range(self.num_spaces)]
        #self.shortcuts[3] = 50
        #self.shortcuts[20] = 30

    def next_space(self, current_space, card_color):
        @todo - find index of next card_color (or wrap if special space)
              - handle lose a turn, and shortcuts
              - return new space at end of turn
        return 
             
