class Player:
    """Class defining the attributes of a player"""
    
    def __init__(self, player_num):
        # Store the player number
        self.player_num = player_num

        # Current space on board
        self.board_idx = -1;
        
        # Member to know whether player is missing the next
        # turn
        self.skip_turn = False
        
    def print(self):
        print("Player " + str(self.player_num) + ":")
        print("\tBoard index: " + str(self.board_idx))
        print("\tSkip Turn: " + str(self.skip_turn))

    def getAndClearSkipTurn(self):
        # Store the value of skip_turn for the return code
        __skip_turn = self.skip_turn

        # Clear skip_turn
        self.skip_turn = False
        
        return __skip_turn

    def move(self, new_board_idx):
        self.board_idx = new_board_idx
