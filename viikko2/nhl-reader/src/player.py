class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']


    def __str__(self):
        pri = f"{self.name:20} {self.team:4}  {self.goals:2} + {self.assists:2} = {self.assists+self.goals}"
        return pri
