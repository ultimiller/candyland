from board import Board

b = Board()
num_spaces = len(b.space_colors)

for i in range(num_spaces):
    print("Space: " + str(i))
    print("\tColor list: " + b.space_colors[i])
    print("\tSpace inst color: " + b.spaces[i].color)
    print("\tSpace inst board_idx: " + str(b.spaces[i].board_idx))
    print("\tSpace inst shortcut_idx: " + str(b.spaces[i].shortcut_idx))
    print("\tSpace inst lose_turn: " + str(b.spaces[i].lose_turn))
    
