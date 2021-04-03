from board import Board
from deck import Deck
from player import Player
from stats import Stats

#@todo:
#- Add statistics plotting

num_players = 4
num_loops = 10000

# Create the board
b = Board()

# Create a shuffled deck
d = Deck()

# Create players
p = []
for i in range(num_players):
    p.append(Player(i))

# Create a statistics class
s = Stats()

for game_idx in range(num_loops):
    # Reshuffle at the start of each game
    d.shuffle()
    
    # Reset the players state at the start of each game
    for i in range(num_players):
        p[i].reset()

    current_player = 0
    turn_count = 0

    # Take turns, play game
    # Set up an infinite loop that breaks when a player wins.
    while (True):
        if (current_player == 0):
            turn_count += 1
        
        # Check to see if this player's turn is getting skipped
        if (p[current_player].skip_turn):
            p[current_player].set_skip(False)
            # Next players turn
            current_player = (current_player + 1) % num_players
            continue
        
        card = d.draw()
        
        # The board next_space function will update the player board_idx,
        # and return True if this player wins on this move.
        if (b.next_space(p[current_player], card)):
            break
    
        # Next players turn
        current_player = (current_player + 1) % num_players
    
    s.endGame(current_player, turn_count)

s.print()
