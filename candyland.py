from board import Board
from deck import Deck
from player import Player

num_players = 4

# Create the board
b = Board()

# Create a shuffled deck
d = Deck()

# Create players
p = []
for i in range(num_players):
    p.append(Player(i))
current_player = 0

####  DEBUG PRINTS  ####
if (False):
    # Print Spaces (debug)
    for i in range(b.num_spaces):
        print("Space: " + str(i))
        print("\tColor list: " + b.space_colors[i])

        # Print Cards (debug)
        d.print()

        # Print Players (debug)
        for i in range(num_players):
            p[i].print()
####  END DEBUG PRINTS  ####


# Take turns, play game
game_over = False
while (not game_over):
    print("Player " + str(current_player) + "'s turn")
    card = d.draw()
    card.print()
    current_space = p[current_player].board_idx
    next_space = b.next_space(current_space, card.color)
    print("Moving from " + str(current_space) + " to " + str(next_space))
    p[current_player].move(next_space)
    if (p[current_player].current_space >= b.num_spaces):
        game_over = True
    else:
        current_player = (current_player + 1) % num_players
