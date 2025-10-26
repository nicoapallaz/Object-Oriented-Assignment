class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def toString(self):
        return str(self.playerName) + " " + str(self.playerPosition)

class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList

    def toString(self):
        return "" + str(self.teamName)

joe = Player("Joe Montana", "QB")
barry = Player("Barry Sanders", "RB")
goat = Player("Jerry Rice", "WR")
graham = Player("Graham Gano", "K")
team = [joe, barry, goat, graham]
legacyTeam = NFLTeam("Legacy Team", team)

print(legacyTeam.toString())
for player in legacyTeam.playerList:
    print(player.toString())