class Player:
    def __init__(self, name, position):
        self.playerName = name
        self.playerPosition = position

    def __str__(self):
        return f"{self.playerName} {self.playerPosition}"

class NFLTeam:
    def __init__(self, name, players):
        self.teamName = name
        self.playerList = players

    def __str__(self):
        players_str = ""
        for p in self.playerList:
            players_str += "\t" + str(p) + "\n"
        return "\n" + self.teamName + ":\n" + players_str

if __name__ == "__main__":
    qb = Player("Joe Montana", "QB")
    rb = Player("Barry Sanders", "RB")
    wr = Player("Jerry Rice", "WR")
    k = Player("Graham Gano", "K")
    players = [qb, rb, wr, k]
    team = NFLTeam("San Francisco 49ers", players)
    print(team)

