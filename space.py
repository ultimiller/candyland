class Space:
    """Class with attributes for a single board space"""

    # Constructor
    # Board idx and color must be specified.
    def __init__(self, board_idx, color, shortcut_idx=-1, lose_turn=False):
        self.board_idx = board_idx
        self.color = color
        self.shortcut_idx = shortcut_idx
        self.lose_turn = lose_turn
