import PLAYERS
import WAR
from PLAYERS import PLAYER_BASE 
from WAR import War 

while True:
    number_of_games=int(input("Enter the numbers of games: "))
    number_of_players=int(input("Enter the numbers of players: "))  
    number_of_cards=int(input("Please enter the number of cards: "))
    players=PLAYER_BASE(number_of_players,number_of_games,number_of_cards)
    game=War(players.give_cards(),players.give_pack(),players.give_name())
    while number_of_games>0:
            game.shuffle()
            # game.create_player(players.give_name())
            game.deal()
            game.game()
            game.display()
            game.excel()
            number_of_games-=1
    ask=input("Do you want to delete a data? Y/N ")
    answer=ask.lower()
    if answer=="y":
        game.clear() 

