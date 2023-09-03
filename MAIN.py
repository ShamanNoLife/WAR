import PLAYERS
import WAR
from PLAYERS import PLAYER_BASE 
from WAR import War 

while True:
    number_of_games=int(input("Enter the numbers of games: "))
    number_of_players=int(input("Enter the numbers of players: "))  
    number_of_cards=int(input("Please enter the number of cards: "))
    players=PLAYER_BASE(number_of_players,number_of_games,number_of_cards)
    while number_of_players>0:
        name = input("Enter player name: ")
        players.add_player(name)
        number_of_players-=1
    game=War(players.give_cards(),players.give_pack(),players.give_number_of_players())
    while number_of_games>0:
            game.shuffle()
            game.deal()
            game.game()
            game.display()
            game.excel()
            number_of_games-=1
    ask=input("Do you want to delete a data? Y/N ")
    answer=ask.lower()
    if answer=="y":
        game.clear() 

