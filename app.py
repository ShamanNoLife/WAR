""" Utworzenie talii """
ilosc_kart=range(13)
talia_kart=[]
for karta in ilosc_kart:
        for kolor in range(4):
            talia_kart.append(karta+1)           
# print(talia_kart) 

""" Losowanie """
import random
random.shuffle(talia_kart)
index=26
gracz_1=talia_kart[index:]
gracz_2=talia_kart[:index]
# print(gracz_1)
# print(gracz_2)

""" Wojna """
n_karta_g1=[]
n_karta_g2=[]

for karta_gracza_1, karta_gracza_2 in zip(gracz_1, gracz_2):
    if karta_gracza_1>karta_gracza_2:
        #gracz_1.remove(karta_gracza_1)
        gracz_2.remove(karta_gracza_2)
        gracz_1.append(karta_gracza_2)

    elif  karta_gracza_1<karta_gracza_2:
        gracz_1.remove(karta_gracza_1)
        gracz_2.append(karta_gracza_1)
       # gracz_2.remove(karta_gracza_2)

    else:
        gracz_1.remove(karta_gracza_1)
        gracz_2.remove(karta_gracza_2)
        continue

if len(gracz_2)==0:
     print("Wygrał gracz 1")
elif len(gracz_1)==0 :
    print("Wygrał gracz 2")
  
         
    
