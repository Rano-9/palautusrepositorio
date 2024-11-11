from player import Player

class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
        self.players = []
        for i in reader.response:
            player = Player(i)
            self.players.append(player)
    
    def top_scorers_by_nationality(self,nat):
        top_scorers = []
        for i in self.players:
            if i.nationality == nat:
                top_scorers.append(i)
        return sorted(top_scorers, key=lambda i : (i.goals + i.assists),reverse=True)
        