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

number_of_players=int(input("Enter the numbers of players: "))
number_of_games=int(input("Enter the numbers of games: "))

players=Players(number_of_players,number_of_games)

list_of_players=[]
while  number_of_players>0: 
    player_name=input("Enter you'r name: ")
    list_of_players.append(player_name)
    number_of_players-=1
    if players.check_names(list_of_players):
        players.name(list_of_players)
    else:
            print("Duplicate names found. Please provide different names.")
