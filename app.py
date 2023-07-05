class Gra_w_wojne:
    def tasowanie(self):
        ilosc_kart=self.ilosc
        talia_kart=[]
        for karta in range(ilosc_kart):
            for kolor in range(4):
                    talia_kart.append(karta+1)  
        self.talia_po_tas=talia_kart
        return(talia_kart)
    def rozdanie(self):
        talia_kart=self.talia_po_tas
        index=self.talia_gracza
        import random
        random.shuffle(talia_kart)
        gracz_1=talia_kart[index:]
        gracz_2=talia_kart[:index]
        self.talia_gracza_1=gracz_1
        self.talia_gracza_2=gracz_2
    def gra(self):
        import random
        gracz_1=self.talia_gracza_1
        gracz_2=self.talia_gracza_2
        new_t1=[]
        new_t2=[]
        while True:
            if (len(gracz_1)!=0) and (len(gracz_2)!=0 and ((len(new_t1)==0) or (len(new_t2)==0))):
                for karta_gracza_1, karta_gracza_2 in zip(gracz_1, gracz_2):
                    if karta_gracza_1>karta_gracza_2:
                        gracz_1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                        new_t1.append(karta_gracza_1)
                        new_t1.append(karta_gracza_2)
                    elif  karta_gracza_1<karta_gracza_2:
                        gracz_1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                        new_t2.append(karta_gracza_1)
                        new_t2.append(karta_gracza_2)
                    else:
                        gracz_1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                    random.shuffle(new_t1)
                    random.shuffle(new_t2)
            elif (len(gracz_1)!=0) and (len(new_t2)!=0):
                for karta_gracza_1, karta_gracza_2 in zip( gracz_1, new_t2):
                    if karta_gracza_1>karta_gracza_2:
                        gracz_1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                        new_t1.append(karta_gracza_1)
                        new_t1.append(karta_gracza_2)
                    elif  karta_gracza_1<karta_gracza_2:
                        gracz_1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                        gracz_2.append(karta_gracza_1)
                        gracz_2.append(karta_gracza_2)
                    else:
                        gracz_1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                    random.shuffle(gracz_1)
                    random.shuffle(new_t2)           
            elif (len(gracz_2)!=0) and (len(new_t1)!=0):
                for karta_gracza_1, karta_gracza_2 in zip(new_t1,gracz_2):
                    if karta_gracza_1>karta_gracza_2:
                        new_t1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                        gracz_1.append(karta_gracza_1)
                        gracz_1.append(karta_gracza_2)
                    elif  karta_gracza_1<karta_gracza_2:
                        new_t1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                        new_t2.append(karta_gracza_1)
                        new_t2.append(karta_gracza_2)
                    else:
                        new_t1.remove(karta_gracza_1)
                        gracz_2.remove(karta_gracza_2)
                    random.shuffle(new_t1)
                    random.shuffle(gracz_2)            
            elif (len(gracz_1)==0) and (len(gracz_2)==0) and ((len(new_t1)!=0) and (len(new_t2)!=0)):   
                for karta_gracza_1, karta_gracza_2 in zip( new_t1, new_t2):
                    if karta_gracza_1>karta_gracza_2:
                        new_t1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                        gracz_1.append(karta_gracza_1)
                        gracz_1.append(karta_gracza_2)
                    elif  karta_gracza_1<karta_gracza_2:
                        new_t1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                        gracz_2.append(karta_gracza_1)
                        gracz_2.append(karta_gracza_2)
                    else:
                        new_t1.remove(karta_gracza_1)
                        new_t2.remove(karta_gracza_2)
                    random.shuffle(new_t1)
                    random.shuffle(new_t2)
            else:
                break
        self.koniec_g1=gracz_1
        self.koniec_g2=gracz_2
        self.koniec_t1=new_t1
        self.koniec_t2=new_t2
    def wyswietlnanie(self):
        pass
        gracz_1=self.koniec_g1
        gracz_2=self.koniec_g2
        new_t1=self.koniec_t1
        new_t2=self.koniec_t2
        print("Ilość kart gracza 1:",(len(gracz_1)+len(new_t1)))
        print("Ilość kart gracza 2:",(len(gracz_2)+len(new_t2)))
        if len(gracz_2)==0 and len(new_t2)==0:
            print("Wygrał gracz 1")
        elif len(gracz_1)==0 and len(new_t1)==0:
            print("Wygrał gracz 2")
        else:
            print("Remis")
    def __init__(self,ilosc,talia_gracza):
        self.ilosc=ilosc
        self.talia_gracza=talia_gracza        


a=Gra_w_wojne(13,26)
a.tasowanie()
a.rozdanie()
a.gra()
a.wyswietlnanie()



