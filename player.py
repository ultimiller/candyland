class Player:
    """Class defining the attributes of a player"""
    
    def __init__(self, player_num):
        # Store the player number
        self.player_num = player_num
        
        # Assign unique color based on player_num input
        color_opts = ['blue', 'red', 'yellow', 'green']
        self.color = color_opts[player_num]

        # Member to know whether player is missing the next
        # turn
        self.skip_turn = False
        
    def print(self):
        print("Player " + str(self.player_num) + ":")
        print("\tColor: " + self.color)
        print("\tSkip Turn: " + str(self.skip_turn))

    def getAndClearSkipTurn(self):
        # Store the value of skip_turn for the return code
        __skip_turn = self.skip_turn

        # Clear skip_turn
        self.skip_turn = False
        
        return __skip_turn
