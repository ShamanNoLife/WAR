import PLAYERS
import WAR
from WAR import War
from PLAYERS import Players 


#number_of_players=int(input("Enter the numbers of players: "))
number_of_players=2
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

print("Please enter the number of cards: ")
number_of_cards=int(input())
player_pack=number_of_cards*2
game=War(number_of_cards,player_pack,number_of_games)
while number_of_games>0:
    game.shuffle()
    game.deal()
    game.game()
    game.display()
    game.excel()
    number_of_games-=1

