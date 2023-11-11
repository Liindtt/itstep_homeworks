class IteratorTeam:
    def __init__(self):
        self.team = Team()
        self.player_index = 0

    def __next__(self):
        players = self.team.juniors + self.team.seniors

        if self.player_index < len(players):
            curr_player = self.player_index
            self.player_index += 1
            return players[curr_player]
        else:
            raise StopIteration

class Team:
    def __init__(self):
        self.juniors = ["JPlayer1", "JPlayer2", "JPlayer3", "JPlayer4", "JPlayer5"]
        self.seniors = ["Player1", "Player2", "Player3", "Player4"]

    def __iter__(self):
        return IteratorTeam()


for x in Team():
    print(x)
