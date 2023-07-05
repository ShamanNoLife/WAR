class War:
    def shuffle(self):
        number_of_cards=self.number_of_cards
        pack=[]
        for card in range(number_of_cards):
            for card_suit in range(4):
                    pack.append(card+1)  
        self.pack_after_shuffle=pack
        return(pack)
    def deal(self):
        pack=self.pack_after_shuffle
        index=self.player_pack
        import random
        random.shuffle(pack)
        player_1=pack[index:]
        player_2=pack[:index]
        self.player_pack_1=player_1
        self.player_pack_2=player_2
    def game(self):
        import random
        player_1=self.player_pack_1
        player_2=self.player_pack_2
        new_player_1=[]
        new_player_2=[]
        while True:
            if (len(player_1)!=0) and (len(player_2)!=0 and ((len(new_player_1)==0) or (len(new_player_2)==0))):
                for card_player_1, card_player_2 in zip(player_1, player_2):
                    if card_player_1>card_player_2:
                        player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                        new_player_1.append(card_player_1)
                        new_player_1.append(card_player_2)
                    elif  card_player_1<card_player_2:
                        player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                        new_player_2.append(card_player_1)
                        new_player_2.append(card_player_2)
                    else:
                        player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                    random.shuffle(new_player_1)
                    random.shuffle(new_player_2)
            elif (len(player_1)!=0) and (len(new_player_2)!=0):
                for card_player_1, card_player_2 in zip( player_1, new_player_2):
                    if card_player_1>card_player_2:
                        player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                        new_player_1.append(card_player_1)
                        new_player_1.append(card_player_2)
                    elif  card_player_1<card_player_2:
                        player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                        player_2.append(card_player_1)
                        player_2.append(card_player_2)
                    else:
                        player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                    random.shuffle(player_1)
                    random.shuffle(new_player_2)           
            elif (len(player_2)!=0) and (len(new_player_1)!=0):
                for card_player_1, card_player_2 in zip(new_player_1,player_2):
                    if card_player_1>card_player_2:
                        new_player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                        player_1.append(card_player_1)
                        player_1.append(card_player_2)
                    elif  card_player_1<card_player_2:
                        new_player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                        new_player_2.append(card_player_1)
                        new_player_2.append(card_player_2)
                    else:
                        new_player_1.remove(card_player_1)
                        player_2.remove(card_player_2)
                    random.shuffle(new_player_1)
                    random.shuffle(player_2)            
            elif (len(player_1)==0) and (len(player_2)==0) and ((len(new_player_1)!=0) and (len(new_player_2)!=0)):   
                for card_player_1, card_player_2 in zip( new_player_1, new_player_2):
                    if card_player_1>card_player_2:
                        new_player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                        player_1.append(card_player_1)
                        player_1.append(card_player_2)
                    elif  card_player_1<card_player_2:
                        new_player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                        player_2.append(card_player_1)
                        player_2.append(card_player_2)
                    else:
                        new_player_1.remove(card_player_1)
                        new_player_2.remove(card_player_2)
                    random.shuffle(new_player_1)
                    random.shuffle(new_player_2)
            else:
                break
        self.end_player_1=player_1
        self.end_player_2=player_2
        self.end_player_new_pack_1=new_player_1
        self.end_player_new_pack_2=new_player_2
    def display(self):
        player_1=self.end_player_1
        player_2=self.end_player_2
        new_player_1=self.end_player_new_pack_1
        new_player_2=self.end_player_new_pack_2
        print("Number of cards for player 1: ",(len(player_1)+len(new_player_1)))
        print("Number of cards for player 2: ",(len(player_2)+len(new_player_2)))
        if len(player_1)!=0 and len(new_player_1)!=0 and len(player_2)==0 and len(new_player_2)==0:
            print("Player 1 won")
        elif len(player_1)==0 and len(new_player_1)==0 and len(player_2)!=0 and len(new_player_2)!=0:
            print("Player 2 won")
        elif len(player_1)==0 and len(new_player_1)==0 and len(player_2)==0 and len(new_player_2)==0:
            print("DRAW")
    def __init__(self,number_of_cards,player_pack):
        self.number_of_cards=number_of_cards
        self.player_pack=player_pack        

print("Please enter the number of cards: ")
number_of_cards=int(input())
player_pack=number_of_cards*2
game=War(number_of_cards,player_pack)
game.shuffle()
game.deal()
game.game()
game.display()



