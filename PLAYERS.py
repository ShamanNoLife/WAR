class PLAYER_BASE:
    def __init__(self,number_of_players, number_of_games,number_of_cards):
        self.number_of_players=number_of_players
        self.number_of_games=number_of_games
        self.number_of_cards=number_of_cards
    def give_name(self):
        return self.number_of_players
        # number_of_players=self.number_of_players
        # list_of_names=[]
        # while number_of_players>0:
        #     name= input("Enter you'r name: ")
        #     list_of_names.append(name)
        # return list_of_names
    def give_cards(self):
        return self.number_of_cards
    def give_pack(self):
        return self.number_of_cards*2
    def give_games(self):
        return self.number_of_games




