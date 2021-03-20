from space import Space

class Board:

    def __init__(self):
        # Keep the ordered board colors in a list for quick searches for the next
        # space after each turn.
        self.space_colors = ['blue', 'red', 'yellow', 'green', 'blue', 'red', 'yellow', 'green']

        # Convenience member
        self.num_spaces = len(self.space_colors)
        
        self.spaces = []
        # First assign the color and board index to each space
        for i, val in enumerate(self.space_colors):
            self.spaces.append(Space(board_idx=i, color=val))
        
        # Override the exceptions for lose a turn, shortcuts
