from board import Board
from deck import Deck
from player import Player

#@todo:
#- Add logger levels (https://docs.python.org/3/howto/logging.html)
#- Add statistics class (num_turns, winning_player[])
#- Add monte carlo num_runs loop
#- Add statistics plotting

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

# Take turns, play game
# Set up an infinite loop that breaks when a player wins.
while (True):
    print("Player " + str(current_player) + "'s turn")

    # Check to see if this player's turn is getting skipped
    if (p[current_player].skip_turn):
        print("** Turn skipped!")
        p[current_player].set_skip(False)
        # Next players turn
        current_player = (current_player + 1) % num_players
        continue
    
    card = d.draw()
    card.print()
    
    # The board next_space function will update the player board_idx,
    # and return True if this player wins on this move.
    if (b.next_space(p[current_player], card)):
        break

    print("Moving to board space " + str(p[current_player].board_idx))
    # Next players turn
    current_player = (current_player + 1) % num_players

print("Player " + str(current_player) + " WINS!")
