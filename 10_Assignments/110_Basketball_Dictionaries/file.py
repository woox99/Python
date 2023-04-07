players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {"name": "", "age": 16, "position": "P", "team": "en"},
]

class Player:
    def __init__(self, single_player):
        self.name = single_player["name"]
        self.age = single_player["age"]
        self.position = single_player["position"]
        self.team = single_player["team"]

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for i in range(len(team_list)):
            new_team.append(cls(team_list[i]))
        return new_team

player_kevin = Player(players[0])
player_jason = Player(players[1])
player_kyrie = Player(players[2])
player_damian = Player(players[3])
player_joel = Player(players[4])

new_team = Player.get_team(players)
# print(new_team[0].name)


