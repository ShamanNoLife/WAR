class Players:
    def check_names(self,names):
        unique_names = set(names)  
        return len(names) == len(unique_names)
    def name(self,name):
        list=[]
        number=self.number_of_players
        while (number>0):
            list.append(name)
            number-=1
        return list
    def amount_fo_games(self):
         number=self.number_of_games
         return number
    def __init__(self,number_of_players, number_of_games):
        self.number_of_players=number_of_players
        self.number_of_games=number_of_games


