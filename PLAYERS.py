class PLAYER_DATA:
    def __init__(self, name):
        self.name = name
        self.score = 0
    def pack_of_cards(self,pack):
        self.pack=pack
    def update_score(self, points):
        self.score += points

class PLAYER_BASE:
    def __init__(self,number_of_players, number_of_games,number_of_cards,number_of_copies_of_cards):
        self.players = []
        self.number_of_players=number_of_players
        self.number_of_games=number_of_games
        self.number_of_cards=number_of_cards
        self.number_of_copies_of_cards=number_of_copies_of_cards
    def give_number_of_players(self):
        return self.number_of_players
    def give_cards(self):
        return self.number_of_cards
    def give_pack(self):
        return self.number_of_cards*self.number_of_copies_of_cards
    def give_games(self):
        return self.number_of_games
    def add_player(self, name):
        new_player = PLAYER_DATA(name)
        self.players.append(new_player)



