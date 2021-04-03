class Stats:

    def __init__(self):
        self.num_turns = []
        self.winning_players = []

    def endGame(self, winning_player, turn_count):
        self.num_turns.append(turn_count)
        self.winning_players.append(winning_player)

    def print(self):
        turn_sum = 0
        max_turns = 0
        for i in range(len(self.num_turns)):
            turn_sum += self.num_turns[i]
            if (self.num_turns[i] > max_turns):
                max_turns = self.num_turns[i]
                
        print("Mean num turns: " +  str(turn_sum / len(self.num_turns)))
        print("Max num turns: " +  str(max_turns))

        player_wins = [0, 0, 0, 0]
        for i in range(len(self.winning_players)):
            player_wins[self.winning_players[i]] += 1
        print("Winning Percentage by Player:")
        for i in range(len(player_wins)):
            print("Player " + str(i) + ": " + str(player_wins[i]))

