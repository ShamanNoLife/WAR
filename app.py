""" Utworzenie talii """
ilosc_kart=range(54)
talia_kart=[]
for karta in ilosc_kart:
        for kolor in range(4):
            talia_kart.append(karta+1)           
# print(talia_kart) 

""" Losowanie """
import random
random.shuffle(talia_kart)
index=108
gracz_1=talia_kart[index:]
gracz_2=talia_kart[:index]
# print(len(gracz_1))
# print(len(gracz_2))

""" Wojna """
punkty_g1=0
punkty_g2=0
for karta_gracza_1, karta_gracza_2 in zip(gracz_1, gracz_2):
    if karta_gracza_1>karta_gracza_2:
        punkty_g1+=1
        gracz_1.remove(karta_gracza_1)
        gracz_2.remove(karta_gracza_2)
    elif karta_gracza_1<karta_gracza_2:
        punkty_g2+=1
        gracz_1.remove(karta_gracza_1)
        gracz_2.remove(karta_gracza_2)
    else:
        gracz_1.remove(karta_gracza_1)
        gracz_2.remove(karta_gracza_2)
        continue

if punkty_g1>punkty_g2:
     przewaga_g1=punkty_g1-punkty_g2
     print("Wygrał gracz 1 z przewagą ",przewaga_g1)
elif punkty_g1<punkty_g2:
    przewaga_g2=punkty_g2-punkty_g1
    print("Wygrał gracz 2 z przewagą ",przewaga_g2)
else:
     print("Remis")   
         
    
