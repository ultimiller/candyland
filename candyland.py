from board import Board
from deck import Deck

num_players = 4

# Create the board
b = Board()

# Create a shuffled deck
d = Deck()

# Print Spaces (debug)
for i in range(b.num_spaces):
    print("Space: " + str(i))
    print("\tColor list: " + b.space_colors[i])
    print("\tSpace inst color: " + b.spaces[i].color)
    print("\tSpace inst board_idx: " + str(b.spaces[i].board_idx))
    print("\tSpace inst shortcut_idx: " + str(b.spaces[i].shortcut_idx))
    print("\tSpace inst lose_turn: " + str(b.spaces[i].lose_turn))

# Print Cards (debug)
d.print()
