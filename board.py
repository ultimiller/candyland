class Board:

    def __init__(self):
        # Keep the ordered colors of each board space in a list for quick
        # searches for the next space after each turn.
        self.colors = [
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'cupcake', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green', 'ice_cream',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'gummy', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'gingerbread', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'lollipop', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green', 'popsicle',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'chocolate', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green',
            'red', 'purple', 'yellow', 'blue', 'orange', 'green']

        # Number of spaces before the end (Candy Castle)
        self.num_spaces = len(self.colors)

        # Set an array for handling lose-a-turn spots
        self.lose_turns = [False for i in range(self.num_spaces)]
        self.lose_turns[44] = True
        self.lose_turns[75] = True

        # Set an array for handling shortcuts on the board.
        # Default each space's shortcut value to -1, and for the 2 shortcut spaces
        # set the shortcut value to the board index of the space jumped to.
        self.shortcuts = [-1 for i in range(self.num_spaces)]
        self.shortcuts[3] = 59 # Peppermint Pass
        self.shortcuts[28] = 40 # Gummy Pass

    def next_space(self, p, c):
        # Move the player's board_idx based on the card.
        # Return True if this results in the player winning, False otherwise.

        # Use the list index method to find the next board space, relative to current_space.
        # If the space doesn't exist, the player either wins or is going backward due to a
        # special card. Python will throw a ValueError exception in this case.
        # Put this in a for loop to handle a card with a double color.
        current_space = p.board_idx
        if (c.special):
            print("** Special Card!")
        c.print
            
        for i in range(c.num_squares):
            try:
                next_space = self.colors.index(c.color, current_space+1)
            except ValueError:
                if (c.special):
                    # Special cards only have 1 matching board index, so search from the
                    # start of the board
                    next_space = self.colors.index(c.color)
                else:
                    # This is just a color card, which means the current player wins!
                    # Set next_space to the Candy Castle space
                    next_space = self.num_spaces
                    
	    # Update the local current_space variable in case this is the
	    # first color on a double color card.
            current_space = next_space

        # Set return code: True if current move finished the game
        if (next_space == self.num_spaces):
            return True

        # Check to see if this is a lose-a-turn (Licorice) space
        if (self.lose_turns[next_space]):
            p.set_skip(True)
        
        # Handle shortcuts
        if (self.shortcuts[next_space] > 0):
            print("** Shortcut! Jumping from " + str(next_space) + " to " +
                  str(self.shortcuts[next_space]))
            next_space = self.shortcuts[next_space]

        p.move(next_space)
        # Set default return code: False because current move did not end game
        return False
             
