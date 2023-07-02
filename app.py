""" Utworzenie talii """
ilosc_kart=range(13)
talia_kart=[]
for karta in ilosc_kart:
        for kolor in range(4):
            talia_kart.append(karta+1)           
# print(talia_kart) 
# print(len(talia_kart))


""" Losowanie """
import random
random.shuffle(talia_kart)
index=26
gracz_1=talia_kart[index:]
gracz_2=talia_kart[:index]
# print(gracz_1)
# print(gracz_2)
# print(len(gracz_1))
# print(len(gracz_2))


""" Wojna """
new_t1=[]
new_t2=[]
while True:

    if (len(gracz_1)!=0) and (len(gracz_2)!=0):
        for karta_gracza_1, karta_gracza_2 in zip(gracz_1, gracz_2):
            if karta_gracza_1>karta_gracza_2:
                win_k=karta_gracza_2
                gracz_1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                new_t1.append(karta_gracza_2)
            elif  karta_gracza_1<karta_gracza_2:
                win_k=karta_gracza_1
                gracz_1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                new_t2.append(karta_gracza_1)
            else:
                gracz_1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                continue

    elif ((len(gracz_1)!=0) and (len(new_t2)!=0)):
        for karta_gracza_1, karta_gracza_2 in zip( gracz_1, new_t2):
            if karta_gracza_1>karta_gracza_2:
                gracz_1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                new_t1.append(karta_gracza_2)
            elif  karta_gracza_1<karta_gracza_2:
                gracz_1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                gracz_2.append(karta_gracza_1)
            else:
                gracz_1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                continue

    elif ((len(gracz_2)!=0) and (len(new_t1)!=0)):
        for karta_gracza_1, karta_gracza_2 in zip(new_t1,gracz_2):
            if karta_gracza_1>karta_gracza_2:
                new_t1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                gracz_1.append(karta_gracza_2)
            elif  karta_gracza_1<karta_gracza_2:
                new_t1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                new_t2.append(karta_gracza_1)
            else:
                new_t1.remove(karta_gracza_1)
                gracz_2.remove(karta_gracza_2)
                continue
    
    elif (len(gracz_1)==0) and (len(gracz_2)==0):   
        for karta_gracza_1, karta_gracza_2 in zip( new_t1, new_t2):
            if karta_gracza_1>karta_gracza_2:
                new_t1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                gracz_1.append(karta_gracza_2)
            elif  karta_gracza_1<karta_gracza_2:
                new_t1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                gracz_2.append(karta_gracza_1)
            else:
                new_t1.remove(karta_gracza_1)
                new_t2.remove(karta_gracza_2)
                continue 
    elif ((len(gracz_1)==0 and len(new_t1)==0)) or (((len(gracz_2)==0) and len(new_t2)==0)):
        break
    else:
        print("Erorr")
        break
    
""" Wyświetlanie wyniku """
print("Ilość kart gracza 1:",(len(gracz_1)+len(new_t1)))
print("Ilość kart gracza 2:",(len(gracz_2)+len(new_t2)))
if len(gracz_2)==0 and len(new_t2)==0:
     print("Wygrał gracz 1")
elif len(gracz_1)==0 and len(new_t1)==0:
    print("Wygrał gracz 2")
  
         
    
